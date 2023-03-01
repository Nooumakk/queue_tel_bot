from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from tele_bot.middleware import _

__all__ = ("ikb_brest_bus", "ikb_brest_passenger", "ikb_brest_cargo", "ikb_brest_ts")


def ikb_brest_bus() -> InlineKeyboardMarkup:
    ikb_brest_bus = InlineKeyboardMarkup(row_width=2)
    ikb1 = InlineKeyboardButton(
        text=_("Место в очереди"), callback_data="brest_place_in_queue_bus"
    )
    ikb2 = InlineKeyboardButton(
        text=_("Длинна очереди"), callback_data="brest_queue_len_bus"
    )
    ikb3 = InlineKeyboardButton(
        text=_("Пропущено за час"), callback_data="brest_an_hour_bus"
    )
    ikb4 = InlineKeyboardButton(
        text=_("Пропущено за сутки"), callback_data="brest_an_day_bus"
    )
    ikb5 = InlineKeyboardButton(text=_("Назад ↩️"), callback_data="back_brest_bus")
    ikb_brest_bus.add(ikb1, ikb2, ikb3, ikb4, ikb5)
    return ikb_brest_bus


def ikb_brest_passenger() -> InlineKeyboardMarkup:
    ikb_brest_passenger = InlineKeyboardMarkup(row_width=2)
    ikb1 = InlineKeyboardButton(
        text=_("Место в очереди"), callback_data="brest_place_in_queue_passenger"
    )
    ikb2 = InlineKeyboardButton(
        text=_("Длинна очереди"), callback_data="brest_queue_len_passenger"
    )
    ikb3 = InlineKeyboardButton(
        text=_("Пропущено за час"), callback_data="brest_an_hour_passenger"
    )
    ikb4 = InlineKeyboardButton(
        text=_("Пропущено за сутки"), callback_data="brest_an_day_passenger"
    )
    ikb5 = InlineKeyboardButton(
        text=_("Назад ↩️"), callback_data="back_brest_passenger"
    )
    ikb_brest_passenger.add(ikb1, ikb2, ikb3, ikb4, ikb5)
    return ikb_brest_passenger


def ikb_brest_cargo() -> InlineKeyboardMarkup:
    ikb_brest_cargo = InlineKeyboardMarkup(row_width=2)
    ikb1 = InlineKeyboardButton(
        text=_("Место в очереди"), callback_data="brest_place_in_queue_cargo"
    )
    ikb2 = InlineKeyboardButton(
        text=_("Длинна очереди"), callback_data="brest_queue_len_cargo"
    )
    ikb3 = InlineKeyboardButton(
        text=_("Пропущено за час"), callback_data="brest_an_hour_cargo"
    )
    ikb4 = InlineKeyboardButton(
        text=_("Пропущено за сутки"), callback_data="brest_an_day_cargo"
    )
    ikb5 = InlineKeyboardButton(text=_("Назад ↩️"), callback_data="back_brest_cargo")
    ikb_brest_cargo.add(ikb1, ikb2, ikb3, ikb4, ikb5)
    return ikb_brest_cargo


def ikb_brest_ts() -> InlineKeyboardMarkup:
    ikb_brest_ts = InlineKeyboardMarkup(row_width=1)
    ikb1 = InlineKeyboardButton(text=_("Автобус 🚌"), callback_data="brest_bus")
    ikb2 = InlineKeyboardButton(
        text=_("Легковой транспорт 🚘"), callback_data="brest_passenger"
    )
    ikb3 = InlineKeyboardButton(
        text=_("Грузовой транспорт 🚛"), callback_data="brest_cargo"
    )
    ikb4 = InlineKeyboardButton(text=_("Назад ↩️"), callback_data="back_brest")
    ikb_brest_ts.add(ikb1, ikb2, ikb3, ikb4)
    return ikb_brest_ts
