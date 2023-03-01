import aiofiles
from datetime import datetime
from bs4 import BeautifulSoup as Bs
from tele_bot.settings import conf
from tele_bot.db.models import User, Numbers
from tele_bot.base.account import BaseUser
from tele_bot.middleware import _


class Parser(BaseUser):
    def __init__(self, checkpoint="bus", transport="bus"):
        self.file_name = (
            conf.BASE_DIR / "daemon" / "pages" / checkpoint / (transport + ".html")
        )

    async def _get_user(self, user_id):
        self._model: User = (
            await User.filter(telegram_id=user_id).prefetch_related().first()
        )

    async def _get_numbers(self, user_id) -> Numbers:
        await self._get_user(user_id)
        try:
            numbers = await self._model.number.values()
        except AttributeError:
            return False
        val = {
            k: v
            for k, v in (await self._model.number.values()).items()
            if k != "id"
            if v is not None
        }
        if val:
            return numbers

    async def _get_transport(self):
        self.transport = []
        self._flag = True
        async with aiofiles.open(self.file_name, mode="r") as file:
            content = await file.read()
            if content != "None":
                result = Bs(content, features="lxml")
                items = result.find("tbody")
                try:
                    for item in items:
                        place = item.select_one("td:nth-child(1)").text.strip()
                        number = item.select_one("td:nth-child(3)").text.strip()
                        edit_status = (
                            item.select_one("td:nth-child(5)").text.strip().split(" ")
                        )
                        time_edit, data_edit = edit_status[0], edit_status[1]
                        status = item.select_one("td:nth-child(6)").text.strip()
                        self.transport.append(
                            {
                                "place": place,
                                "number": number,
                                "time_edit": time_edit,
                                "data_edit": data_edit,
                                "status": status,
                            }
                        )
                except AttributeError:
                    time = datetime.today().strftime("%Y-%m-%d %H:%M")
                    self.response = _("По состоянию на {}:\nОчереди нет").format(time)
            else:
                self._flag = False
                self.response = _("Информация недоступна в данное время")

    async def get_place(self, transport, user_id):
        numbers = await self._get_numbers(user_id)
        await self._get_transport()
        if self.transport:
            if numbers:
                if numbers[transport] != None:
                    for auto in self.transport:
                        if numbers[transport] == auto["number"]:
                            if auto["status"] == "Прибыл в ЗО":
                                time = datetime.today().strftime("%Y-%m-%d %H:%M")
                                self.response = _(
                                    "По состоянию на {time}:\n"
                                    "Ваше авто {place} в очереди"
                                ).format(time=time, place=auto["place"])
                                break
                            elif auto["status"] == "Вызван в ПП":
                                self.response = _(
                                    "Вас вызвали в пункт пропуска, время вызова: {time}\n"
                                    "Дата: {data}"
                                ).format(time=auto["time_edit"], data=auto["data_edit"])
                                break
                            else:
                                self.response = (
                                    "Ваш транспорт аннулирован, время аннулирования: {time}\n"
                                    "Дата: {data}"
                                ).format(time=auto["time_edit"], data=auto["data_edit"])
                                break
                    else:
                        self.response = _("Вы не состоите в очереди")
                else:
                    self.response = _("Вы не привязали номер авто к своему аккаунту")
            else:
                self.response = _("Вы не отслеживаете ни один вид транспорта")
        else:
            time = datetime.today().strftime("%Y-%m-%d %H:%M")
            self.response = _(
                "По состоянию на {}:\nДлинна очереди зоны ожидания - 0"
            ).format(time)

    async def len_queue(self):
        await self._get_transport()
        if self._flag:
            self.queue = 0
            for ts in self.transport:
                if ts["status"] == "Прибыл в ЗО":
                    self.queue += 1
            if self.queue > 0:
                time = datetime.today().strftime("%Y-%m-%d %H:%M")
                self.response = _(
                    "По состоянию на {time}:\nДлинна очереди зоны ожидания - {queue}"
                ).format(time=time, queue=self.queue)
            else:
                time = datetime.today().strftime("%Y-%m-%d %H:%M")
                self.response = _(
                    "По состоянию на {}:\nДлинна очереди зоны ожидания - 0"
                ).format(time)
        else:
            self.response = _("Информация недоступна в данное время")

    async def queue_promotion(self):
        self.promotion = []
        async with aiofiles.open(self.file_name, mode="r") as file:
            content = await file.read()
            if content != "None":
                result = Bs(content, features="lxml")
                items = result.select_one(
                    "div.row.b-shdow.grey-bg > div.noPointer.zoPage > div.v-card__title > div.col-12.pa-0 > div:nth-child(2)"
                )
                for item in items:
                    arg = item.text.split(" ", 1)[0]
                    if arg != "":
                        self.promotion.append(arg)
                time = datetime.today().strftime("%Y-%m-%d %H:%M")
                self.promotion_per_day = _(
                    "По состоянию на {time}:\nПропущено за сутки - {promotion}"
                ).format(time=time, promotion=self.promotion[1])
                self.promotion_per_hour = _(
                    "По состоянию на {time}:\nПропущено за час - {promotion}"
                ).format(time=time, promotion=self.promotion[0])
            else:
                self.promotion_per_day = _("Информация недоступна в данное время")
                self.promotion_per_hour = _("Информация недоступна в данное время")
