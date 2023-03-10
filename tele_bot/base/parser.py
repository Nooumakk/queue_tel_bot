import aiofiles
import json
import asyncio
from datetime import datetime
from tele_bot.settings import conf
from tele_bot.db.models import User, Numbers
from tele_bot.base.account import BaseUser
from tele_bot.middleware import _


class Parser(BaseUser):
    """
    :param file: File name
    :param transport: Transport used
    :param checkpoint: ru name of the checkpoint
    :param user_id: user telergam id

    """

    def __init__(self, file, transport=None, checkpoint=None, user_id=None):
        self.user_id = user_id
        self.transport = transport
        self.checkpoint = checkpoint
        if "stat" not in file and file != "checkpoint":
            self.file_name = conf.BASE_DIR / "checkpoint" / (file + ".json")
        else:
            self.file_name = (
                conf.BASE_DIR / "checkpoint" / "statistic" / (file + ".json")
            )

    async def _get_user(self, user_id):
        self._model: User = await User.filter(telegram_id=user_id).first()

    async def _get_numbers(self, user_id) -> Numbers:
        """
        :return dick of the form: {number: value}

        """
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
    
    async def _get_params(self, auto: dict):
        time_edit, data_edit = (
            auto["changed_date"].strip().split(" ")
        )
        if auto["status"] == 2:
            time = datetime.today().strftime("%Y-%m-%d %H:%M")
            self.response = _(
                "По состоянию на {time}:\n"
                "Ваше авто {place} в очереди"
            ).format(time=time, place=auto["order_id"])
        elif auto["status"] == 3:
            self.response = _(
                "Вас вызвали в пункт пропуска:\nВремя вызова: {time}\n"
                "Дата: {data}"
            ).format(time=time_edit, data=data_edit)
        else:
            self.response = _(
                "Ваш транспорт аннулирован:\nВремя аннулирования: {time}\n"
                "Дата: {data}"
            ).format(time=time_edit, data=data_edit)

    async def get_place(self):
        numbers = await self._get_numbers(self.user_id)
        if numbers:
            if numbers[self.transport]:
                transport = self.transport + "LiveQueue"
                async with aiofiles.open(self.file_name, "r") as file:
                    queue = json.loads(await file.read())[transport]
                    if queue:
                        for auto in queue:
                            if auto["regnum"] == numbers[self.transport]:
                                await self._get_params(auto)
                                break
                        else:
                            self.response = _("Вы не состоите в очереди")
                    else:
                        time = datetime.today().strftime("%Y-%m-%d %H:%M")
                        self.response = _(
                            "По состоянию на {}:\nДлинна очереди зоны ожидания - 0"
                        ).format(time)
            else:
                self.response = _("Вы не привязали номер авто к своему аккаунту")
        else:
            self.response = _("Вы не отслеживаете ни один вид транспорта")

    async def len_queue(self):
        """
        :params checkpoint, transport must be capitalized
        """
        async with aiofiles.open(self.file_name, "r") as file:
            checkpoints = json.loads(await file.read())["result"]
            for checkpoint in checkpoints:
                if checkpoint["name"] == self.checkpoint:
                    ts = "count" + self.transport
                    time = datetime.today().strftime("%Y-%m-%d %H:%M")
                    self.response = _(
                        "По состоянию на {time}:\nДлинна очереди зоны ожидания - {queue}"
                    ).format(time=time, queue=checkpoint[ts])
                    break

    async def _queue_promotion(self):
        """
        File names for checkpoint:

        stat2 - Urbany
        stat3 - Kotlovka
        stat4 - Grigorovshcina
        stat5 - Beniakoni
        stat6 - Kamenny Log
        stat7 - Berestovitsa
        stat8 - Brest
        """
        self.time = datetime.today().strftime("%Y-%m-%d %H:%M")
        async with aiofiles.open(self.file_name, "r") as file:
            res = json.loads(await file.read())
            return res

    async def queue_promotion_per_day(self):
        transport = self.transport + "LastDay"
        checkpoint = await self._queue_promotion()
        self.response = _(
            "По состоянию на {time}:\nПропущено за сутки - {promotion}"
        ).format(time=self.time, promotion=checkpoint[transport])

    async def queue_promotion_per_hour(self):
        transport = self.transport + "LastHour"
        checkpoint = await self._queue_promotion()
        self.response = _(
            "По состоянию на {time}:\nПропущено за час - {promotion}"
        ).format(time=self.time, promotion=checkpoint[transport])
