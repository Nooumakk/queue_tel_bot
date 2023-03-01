import aiofiles
import os
from aiogram import types
from aiogram import types
from tele_bot.db.models import Tracking, Car, Numbers, User
from tele_bot.base.account import BaseUser
from tele_bot.settings import conf
from bs4 import BeautifulSoup as Bs
from tele_bot import keyboard
from aiogram import Bot
from tele_bot.middleware import _
from tele_bot.base.template import _m, _k
from tele_bot import keyboard
from aiogram.dispatcher import FSMContext


class AddMonitoring(BaseUser):
    def __init__(self, user_id):
        self._user_id = user_id

    async def _get_user(self):
        self._model = await User.get(telegram_id=self._user_id)

    async def _get_numbers(self):
        await self._get_user()
        return await self._model.number

    async def _create_keyboard(self):
        self._buttons = []
        val = {
            k: v
            for k, v in (await self._model.number.values()).items()
            if k != "id"
            if v is not None
        }
        if val:
            for num in val:
                if num == "bus_number":
                    self._buttons.append(
                        types.InlineKeyboardButton(
                            text=_("Автобус  {bus_number}  🚌").format(**val),
                            callback_data="bus_monitoring",
                        )
                    )
                elif num == "passenger_number":
                    self._buttons.append(
                        types.InlineKeyboardButton(
                            text=_("Легковая  {passenger_number}  🚘").format(**val),
                            callback_data="passenger_monitoring",
                        )
                    )
                else:
                    self._buttons.append(
                        types.InlineKeyboardButton(
                            text=_("Грузовая  {cargo_number}  🚛").format(**val),
                            callback_data="cargo_monitoring",
                        )
                    )
            self.transport = types.InlineKeyboardMarkup(row_width=1)
            self.transport.add(*self._buttons)
            self.transport.add(
                types.InlineKeyboardButton(
                    text=_("Назад ↩️"), callback_data="back_monitoring"
                )
            )
            return True
        return False

    async def add_monitoring(self):
        numbers: Numbers = await self._get_numbers()
        if not await self._model.monitoring:
            if numbers != None:
                if await self._create_keyboard():
                    self.response = _("Выберите нужный транспорт")
                    return
                self.response = _("Вы не отслеживаете ни один вид транспорта")
                self.transport = keyboard.ikb_back_monitoring()
            else:
                self.response = _("Вы не отслеживаете ни один вид транспорта")
                self.transport = keyboard.ikb_back_monitoring()
        else:
            monitoring: Tracking = await self._model.monitoring
            self.response = _(
                "Уже включен мониторинг для транспорта с номером '{}'"
            ).format(monitoring.number)
            self.transport = keyboard.ikb_back_monitoring()

    async def add_transport(self, ts_id, ts_temp, state: FSMContext):
        numbers: Numbers = await self._get_numbers()
        if ts_id == 1:
            number = numbers.bus_number
        elif ts_id == 2:
            number = numbers.passenger_number
        else:
            number = numbers.cargo_number
        async with state.proxy() as data:
            data["ts"] = ts_id
            data["ts_tem"] = ts_temp
            data["number"] = number
        self.response = _("Выберите частоту уведомлений:")

    async def add_intensity(self, intensity, state: FSMContext):
        async with state.proxy() as data:
            data["intensity"] = intensity
            number: Numbers = data["number"]
        self.response = _(
            "Параметры мониторинга:\n"
            "<b>Номер:</b> {number}\n<b>Вид транспорта:</b> "
            "{data}\n<b>Частота уведомлений:</b> {intensity}"
        ).format(number=number, data=data["ts_tem"], intensity=intensity)


class RegMonitoring(BaseUser):
    def __init__(self, user_id):
        self._user_id = user_id
        self._model: User = None
        self._file_paths = []
        self._checkpoint_ru = None
        self._status = None
        self._flag = False

    async def _get_user(self):
        self._model = await User.get(telegram_id=self._user_id)
        self.lang_code = self._model.language_code

    async def _get_numbers(self):
        await self._get_user()
        return await self._model.number

    async def _get_path(self):
        self._transport = await Car.get(id=self._ts)
        self._file_paths = [
            file.path + "/" + self._transport.transport.strip() + ".html"
            for file in os.scandir(conf.BASE_DIR / "daemon" / "pages")
        ]

    async def _get_monitoring(self):
        await self._get_user()
        return await self._model.monitoring

    async def _get_params(self, state: FSMContext):
        async with state.proxy() as data:
            self._ts = data["ts"]
            self._number = data["number"]
            self._intensity = data["intensity"]
            return {
                "number": data["number"],
                "transport": data["ts"],
                "intensity": data["intensity"],
            }

    async def _get_place_monitoring(self):
        await self._get_path()
        for file_path in self._file_paths:
            async with aiofiles.open(file_path, mode="r") as file:
                content = await file.read()
                if content != "None":
                    result = Bs(content, features="lxml")
                    items = result.find("tbody")
                    if items.text != "Отсутствуют данные":
                        for item in items:
                            number = item.select_one("td:nth-child(3)").text.strip()
                            if self._number != number:
                                continue
                            self._status = item.select_one(
                                "td:nth-child(6)"
                            ).text.strip()
                            if self._status == "Прибыл в ЗО":
                                self._params = {
                                    "number": self._number,
                                    "checkpoint": file_path.split("/")[-2],
                                    "car_id": self._ts,
                                    "intensity": self._intensity,
                                    "place": item.select_one(
                                        "td:nth-child(1)"
                                    ).text.strip(),
                                }
                                self._checkpoint_ru = result.select_one(
                                    ".adress-bar > div:nth-child(1) > h2:nth-child(1)"
                                ).text
                                return await self._get_user(), True
                            await self._get_user()
                            return False
        return False

    async def save(self, state):
        try:
            self._params = await self._get_params(state)
            if await self._get_place_monitoring():
                monitoring = await Tracking.create(**self._params)
                self._model.monitoring = monitoring
                await self._model.save()
                self.response = _(
                    "✅ Мониторинг подключен\n"
                    "<b>Номер:</b> {number}\n"
                    "<b>Пункт пропуска:</b> {checkpoint}\n"
                    "<b>Периодичность:</b> {intensity}\n"
                    "<b>Текущее место в очереди: </b> {place}"
                ).format(
                    number=self._number,
                    checkpoint=_m(self._checkpoint_ru, self.lang_code),
                    intensity=self._intensity,
                    place=self._params["place"],
                )
            else:
                if self._status == None:
                    self.response = _(
                        "❌ Транспорт с номером '{}' не зарегистрирован ни в одной зоне ожидания,"
                        "проверьте правильность введенного номера или повторите попытку через несколько минут"
                    ).format(self._number)
                    return
                self.response = _(
                    "Транспорт имеет статус '{}'\nМониторинг не может быть подключен"
                ).format(_m(self._status, self.lang_code))
        finally:
            await state.finish()

    async def delete(self):
        monitoring: Tracking = await self._get_monitoring()
        if monitoring:
            await monitoring.delete()
            self.response = _(
                "Мониторинг для транспорта с номером '{}' был удален"
            ).format(monitoring.number)
        else:
            self.response = _("Вы не подключали услугу мониторинга")


class Monitoring:
    def __init__(self, model):
        self._flag = False
        self._model: Tracking = model

    async def _get_all_users(self):
        self._users = await self._model.all()
        return self._users

    async def _get_params(self, user: Tracking):
        self._number = user.number
        self._checkpoint = user.checkpoint
        self._intensity = user.intensity
        self._place = user.place
        self._car: Car = await user.car

    async def _get_html(self):
        file_path = (
            conf.BASE_DIR
            / "daemon"
            / "pages"
            / self._checkpoint
            / (self._car.transport.strip() + ".html")
        )
        async with aiofiles.open(file_path, mode="r") as file:
            self._content = await file.read()
            if self._content:
                return True
            return False

    async def search_transport(self, bot):
        if await self._get_all_users():
            for user in self._users:
                await self._get_params(user)
                if await self._get_html():
                    result = Bs(self._content, features="lxml")
                    self._items = result.find("tbody")
                    if self._items:
                        if self._items.text != "Отсутствуют данные":
                            self._user: Tracking = user
                            if await self._search_user():
                                await self.send_message(bot)
                        continue
                continue

    async def _check_status(self):
        if self._status == "Прибыл в ЗО":
            return True

    async def _edit_data(self):
        if self._place != self.new_place:
            if self._place - int(self.new_place) >= self._intensity:
                await self._user.update_from_dict({"place": self.new_place})
                return await self._user.save(), True

    async def _search_user(self):
        for item in self._items:
            number = item.select_one("td:nth-child(3)").text.strip()
            if number != self._number:
                continue
            self._status = item.select_one("td:nth-child(6)").text.strip()
            if await self._check_status():
                self.new_place = item.select_one("td:nth-child(1)").text.strip()
                if await self._edit_data():
                    return True
                return False
            return True
        self._status = "Удален"
        return True

    async def send_message(self, bot: Bot):
        await self._user.fetch_related("user")
        user_id = self._user.user.telegram_id
        lang_code = self._user.user.language_code
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        if await self._check_status():
            await bot.send_message(
                user_id,
                text=_m("Ваш транспорт {} в очереди", lang_code).format(self.new_place),
                reply_markup=kb.add(
                    types.KeyboardButton(text=_k("Главное меню", lang_code))
                ),
            )
        else:
            if self._status == "Вызван в ПП":
                await self._user.delete()
                await bot.send_message(
                    text=_m("Вас вызвали в пункт пропуска", lang_code),
                    chat_id=user_id,
                    reply_markup=kb.add(
                        types.KeyboardButton(text=_k("Главное меню", lang_code))
                    ),
                )
            elif self._status == "Удален":
                await self._user.delete()
                await bot.send_message(
                    text=_m("Вы больше не состоите в очереди", lang_code),
                    chat_id=user_id,
                    reply_markup=kb.add(
                        types.KeyboardButton(text=_k("Главное меню", lang_code))
                    ),
                )
            elif self._status == "Аннулирован":
                await self._user.delete()
                await bot.send_message(
                    text=_m("Ваш транспорт аннулирован", lang_code),
                    chat_id=user_id,
                    reply_markup=kb.add(
                        types.KeyboardButton(text=_k("Главное меню", lang_code))
                    ),
                )


async def start_monitoring(bot: Bot):
    monitoring = Monitoring(Tracking)
    await monitoring.search_transport(bot)
