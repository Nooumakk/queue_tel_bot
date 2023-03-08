import aiofiles
import os
import json
from pathlib import Path
from aiogram import types
from aiogram import types
from tele_bot.db.models import Tracking, Car, Numbers, User
from tele_bot.base.account import BaseUser
from tele_bot.settings import conf
from tele_bot import keyboard
from aiogram import Bot
from tele_bot.middleware import _
from tele_bot.base.template import _m, _k
from tele_bot import keyboard
from aiogram.dispatcher import FSMContext


class AddMonitoring(BaseUser):
    def __init__(self, user_id):
        self._user_id = user_id
        self._model: User = None
        self._file_paths = []
        self._status = None

    async def _get_user(self):
        self._model = await User.get(telegram_id=self._user_id)
        self.lang_code = self._model.language_code

    async def _get_numbers(self):
        await self._get_user()
        return await self._model.number

    async def _get_path(self):
        return [
            file.path
            for file in os.scandir(conf.BASE_DIR / "checkpoint")
            if file.is_file()
        ]

    async def _get_monitoring(self):
        await self._get_user()
        return await self._model.monitoring

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
                if num == "bus":
                    self._buttons.append(
                        types.InlineKeyboardButton(
                            text=_("Автобус  {bus}  🚌").format(**val),
                            callback_data="bus_monitoring",
                        )
                    )
                elif num == "car":
                    self._buttons.append(
                        types.InlineKeyboardButton(
                            text=_("Легковая  {car}  🚘").format(**val),
                            callback_data="passenger_monitoring",
                        )
                    )
                else:
                    self._buttons.append(
                        types.InlineKeyboardButton(
                            text=_("Грузовая  {truck}  🚛").format(**val),
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
                _("Уже включен мониторинг для транспорта с номером '{}'")
            ).format(monitoring.number)
            self.transport = keyboard.ikb_back_monitoring()

    async def add_transport(self, ts_id, ts_temp, state: FSMContext):
        numbers: Numbers = await self._get_numbers()
        if ts_id == 1:
            number = numbers.bus
            transport = "bus"
        elif ts_id == 2:
            number = numbers.car
            transport = "car"
        else:
            number = numbers.truck
            transport = "truck"
        async with state.proxy() as data:
            data["ts_id"] = ts_id
            data["ts_tem"] = ts_temp
            data["number"] = number
            data["transport"] = transport
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

    async def save(self, state):
        try:
            await self._get_params(state)
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
                        " проверьте правильность введенного номера или повторите попытку через несколько минут"
                    ).format(self._number)
                    return
                elif self._status == 3:
                    self.response = _(
                        "Транспорт имеет статус '{}'\nМониторинг не может быть подключен"
                    ).format(_m("Вызван в ПП", self.lang_code))
                else:
                    self._status = "Аннулирован"
                self.response = _(
                    "Транспорт имеет статус '{}'\nМониторинг не может быть подключен"
                ).format(_m("Аннулирован", self.lang_code))
        finally:
            await state.finish()

    async def _get_params(self, state: FSMContext):
        async with state.proxy() as data:
            self._ts_id = data["ts_id"]
            self._number = data["number"]
            self._intensity = data["intensity"]
            self._transport = data["transport"]

    async def _get_place_monitoring(self):
        for file_path in await self._get_path():
            async with aiofiles.open(file_path, mode="r") as file:
                res = json.loads(await file.read())
                transport = self._transport + "LiveQueue"
                if res[transport]:
                    for auto in res[transport]:
                        if self._number == auto["regnum"]:
                            if auto["status"] == 2:
                                self._params = {
                                    "number": self._number,
                                    "checkpoint": Path(file_path).name.split(".")[0],
                                    "car_id": self._ts_id,
                                    "intensity": self._intensity,
                                    "place": auto["order_id"],
                                }
                                self._checkpoint_ru = res["info"]["name"]
                                return await self._get_user(), True
                            await self._get_user()
                            self._status = int(auto["status"])
                            return False
        return False

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
        self._model: Tracking = model

    async def _get_all_users(self):
        self._users = await self._model.all()
        return self._users

    async def _get_params(self, user: Tracking):
        self._number = user.number
        self._checkpoint = user.checkpoint
        self._intensity = user.intensity
        self._place = user.place
        self._car = await user.car

    async def _get_data(self):
        file_path = conf.BASE_DIR / "checkpoint" / (self._checkpoint + ".json")
        async with aiofiles.open(file_path, mode="r") as file:
            transport = self._car.transport + "LiveQueue"
            self._content = json.loads(await file.read())[transport]
            if self._content:
                return True
            return False

    async def search_transport(self, bot):
        if await self._get_all_users():
            for user in self._users:
                await self._get_params(user)
                if await self._get_data():
                    self._user: Tracking = user
                    if await self._search_user():
                        await self.send_message(bot)
                        continue
                    continue
                self._status = 0
                await self.send_message(bot)

    async def _check_status(self):
        """
        status 0: deleted from queue
        status 2: arriver at tge checkpoint
        status 3: called to the checkpoint
        status 9: transport cancelled

        """
        if self._status == 2:
            return True

    async def _edit_data(self):
        if self._place != int(self.new_place):
            if self._place - int(self.new_place) >= self._intensity:
                await self._user.update_from_dict({"place": self.new_place})
                return await self._user.save(), True

    async def _search_user(self):
        for auto in self._content:
            number = auto["regnum"]
            if number != self._number:
                continue
            self._status = int(auto["status"])
            if await self._check_status():
                self.new_place = int(auto["order_id"])
                if await self._edit_data():
                    return True
                return False
            return True
        self._status = 0
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
            if self._status == 3:
                await self._user.delete()
                await bot.send_message(
                    text=_m("Вас вызвали в пункт пропуска", lang_code),
                    chat_id=user_id,
                    reply_markup=kb.add(
                        types.KeyboardButton(text=_k("Главное меню", lang_code))
                    ),
                )
            elif self._status == 0:
                await self._user.delete()
                await bot.send_message(
                    text=_m("Вы больше не состоите в очереди", lang_code),
                    chat_id=user_id,
                    reply_markup=kb.add(
                        types.KeyboardButton(text=_k("Главное меню", lang_code))
                    ),
                )
            elif self._status == 9:
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
