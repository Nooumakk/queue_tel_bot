from aiogram import types
from tele_bot.bot import dp, bot
from tele_bot import keyboard
from aiogram.utils.exceptions import MessageNotModified
from tele_bot.base.parser import Parser
from tele_bot.utils.anti_flod import flood_callback
from tele_bot.middleware import _


__all__ = (
    "kamenny_log_data",
    "back_kamenny_log",
    "kamenny_log_bus",
    "kamenny_log_back_bus",
    "kamenny_log_place_in_queue_bus",
    "kamenny_log_queue_len_bus",
    "kamenny_log_an_hour_bus",
    "kamenny_log_an_day_bus",
    "kamenny_log_passenger",
    "kamenny_log_back_passenger",
    "kamenny_log_place_in_queue_passenger",
    "kamenny_log_queue_len_passenger",
    "kamenny_log_an_hour_passenger",
    "kamenny_log_an_day_passenger",
    "kamenny_log_cargo",
    "kamenny_log_back_cargo",
    "kamenny_log_place_in_queue_cargo",
    "kamenny_log_queue_len_cargo",
    "kamenny_log_an_hour_cargo",
    "kamenny_log_an_day_cargo",
)


@dp.callback_query_handler(text="kamenny_log")
@dp.throttled(flood_callback, rate=1)
async def kamenny_log_data(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=_("Страна: Литва 🇱🇹\nПункт пропуска: Каменный Лог"),
        reply_markup=keyboard.ikb_kamenny_log_ts(),
    )


@dp.callback_query_handler(text="back_kamenny_log")
@dp.throttled(flood_callback, rate=1)
async def back_kamenny_log(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=_("Страна: Литва 🇱🇹\nВыберите пункт пропуска"),
        reply_markup=keyboard.ikb_lithuania(),
    )


@dp.callback_query_handler(text="kamenny_log_bus")
@dp.throttled(flood_callback, rate=1)
async def kamenny_log_bus(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=_("Страна: Литва 🇱🇹\nПункт пропуска: Каменный Лог\nТранспорт: Автобус 🚌"),
        reply_markup=keyboard.ikb_kamenny_log_bus(),
    )


@dp.callback_query_handler(text="back_kamenny_log_bus")
@dp.throttled(flood_callback, rate=1)
async def kamenny_log_back_bus(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=_("Страна: Литва 🇱🇹\nПункт пропуска: Каменный Лог"),
        reply_markup=keyboard.ikb_kamenny_log_ts(),
    )
    await bot.answer_callback_query(callback_query_id=callback.id)


@dp.callback_query_handler(text="kamenny_log_place_in_queue_bus")
@dp.throttled(flood_callback, rate=1)
async def kamenny_log_place_in_queue_bus(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    checkpoint_info = Parser("kamenny_log", "bus")
    await checkpoint_info.get_place("bus_number", user_id)
    try:
        await callback.message.edit_text(
            text=checkpoint_info.response, reply_markup=keyboard.ikb_kamenny_log_bus()
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)
    return checkpoint_info._model


@dp.callback_query_handler(text="kamenny_log_queue_len_bus")
@dp.throttled(flood_callback, rate=1)
async def kamenny_log_queue_len_bus(callback: types.CallbackQuery):
    checkpoint_info = Parser("kamenny_log", "bus")
    await checkpoint_info.len_queue()
    try:
        await callback.message.edit_text(
            text=checkpoint_info.response, reply_markup=keyboard.ikb_kamenny_log_bus()
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)


@dp.callback_query_handler(text="kamenny_log_an_hour_bus")
@dp.throttled(flood_callback, rate=1)
async def kamenny_log_an_hour_bus(callback: types.CallbackQuery):
    checkpoint_info = Parser("kamenny_log", "bus")
    await checkpoint_info.queue_promotion()
    try:
        await callback.message.edit_text(
            text=checkpoint_info.promotion_per_hour,
            reply_markup=keyboard.ikb_kamenny_log_bus(),
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)


@dp.callback_query_handler(text="kamenny_log_an_day_bus")
@dp.throttled(flood_callback, rate=1)
async def kamenny_log_an_day_bus(callback: types.CallbackQuery):
    checkpoint_info = Parser("kamenny_log", "bus")
    await checkpoint_info.queue_promotion()
    try:
        await callback.message.edit_text(
            text=checkpoint_info.promotion_per_day,
            reply_markup=keyboard.ikb_kamenny_log_bus(),
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)


@dp.callback_query_handler(text="kamenny_log_passenger")
@dp.throttled(flood_callback, rate=1)
async def kamenny_log_passenger(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=_("Страна: Литва 🇱🇹\nПункт пропуска: Каменный Лог\nТранспорт: Легковой 🚘"),
        reply_markup=keyboard.ikb_kamenny_log_passenger(),
    )


@dp.callback_query_handler(text="back_kamenny_log_passenger")
@dp.throttled(flood_callback, rate=1)
async def kamenny_log_back_passenger(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=_("Страна: Литва 🇱🇹\nПункт пропуска: Каменный Лог"),
        reply_markup=keyboard.ikb_kamenny_log_ts(),
    )


@dp.callback_query_handler(text="kamenny_log_place_in_queue_passenger")
@dp.throttled(flood_callback, rate=1)
async def kamenny_log_place_in_queue_passenger(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    checkpoint_info = Parser("kamenny_log", "passenger")
    await checkpoint_info.get_place("passenger_number", user_id)
    try:
        await callback.message.edit_text(
            text=checkpoint_info.response,
            reply_markup=keyboard.ikb_kamenny_log_passenger(),
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)
    return checkpoint_info._model


@dp.callback_query_handler(text="kamenny_log_queue_len_passenger")
@dp.throttled(flood_callback, rate=1)
async def kamenny_log_queue_len_passenger(callback: types.CallbackQuery):
    checkpoint_info = Parser("kamenny_log", "passenger")
    await checkpoint_info.len_queue()
    try:
        await callback.message.edit_text(
            text=checkpoint_info.response,
            reply_markup=keyboard.ikb_kamenny_log_passenger(),
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)


@dp.callback_query_handler(text="kamenny_log_an_hour_passenger")
@dp.throttled(flood_callback, rate=1)
async def kamenny_log_an_hour_passenger(callback: types.CallbackQuery):
    checkpoint_info = Parser("kamenny_log", "passenger")
    await checkpoint_info.queue_promotion()
    try:
        await callback.message.edit_text(
            text=checkpoint_info.promotion_per_hour,
            reply_markup=keyboard.ikb_kamenny_log_passenger(),
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)


@dp.callback_query_handler(text="kamenny_log_an_day_passenger")
@dp.throttled(flood_callback, rate=1)
async def kamenny_log_an_day_passenger(callback: types.CallbackQuery):
    checkpoint_info = Parser("kamenny_log", "passenger")
    await checkpoint_info.queue_promotion()
    try:
        await callback.message.edit_text(
            text=checkpoint_info.promotion_per_day,
            reply_markup=keyboard.ikb_kamenny_log_passenger(),
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)


@dp.callback_query_handler(text="kamenny_log_cargo")
@dp.throttled(flood_callback, rate=1)
async def kamenny_log_cargo(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=_(
            "Страна: Литва 🇱🇹\nПункт пропуска: Каменный Лог\nТранспорт: Грузовой  🚛"
        ),
        reply_markup=keyboard.ikb_kamenny_log_cargo(),
    )


@dp.callback_query_handler(text="back_kamenny_log_cargo")
@dp.throttled(flood_callback, rate=1)
async def kamenny_log_back_cargo(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=_("Страна: Литва 🇱🇹\nПункт пропуска: Каменный Лог"),
        reply_markup=keyboard.ikb_kamenny_log_ts(),
    )


@dp.callback_query_handler(text="kamenny_log_place_in_queue_cargo")
@dp.throttled(flood_callback, rate=1)
async def kamenny_log_place_in_queue_cargo(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    checkpoint_info = Parser("kamenny_log", "cargo")
    await checkpoint_info.get_place("cargo_number", user_id)
    try:
        await callback.message.edit_text(
            text=checkpoint_info.response, reply_markup=keyboard.ikb_kamenny_log_cargo()
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)
    return checkpoint_info._model


@dp.callback_query_handler(text="kamenny_log_queue_len_cargo")
@dp.throttled(flood_callback, rate=1)
async def kamenny_log_queue_len_cargo(callback: types.CallbackQuery):
    checkpoint_info = Parser("kamenny_log", "cargo")
    await checkpoint_info.len_queue()
    try:
        await callback.message.edit_text(
            text=checkpoint_info.response, reply_markup=keyboard.ikb_kamenny_log_cargo()
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)


@dp.callback_query_handler(text="kamenny_log_an_hour_cargo")
@dp.throttled(flood_callback, rate=1)
async def kamenny_log_an_hour_cargo(callback: types.CallbackQuery):
    checkpoint_info = Parser("kamenny_log", "cargo")
    await checkpoint_info.queue_promotion()
    try:
        await callback.message.edit_text(
            text=checkpoint_info.promotion_per_hour,
            reply_markup=keyboard.ikb_kamenny_log_cargo(),
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)


@dp.callback_query_handler(text="kamenny_log_an_day_cargo")
@dp.throttled(flood_callback, rate=1)
async def kamenny_log_an_day_cargo(callback: types.CallbackQuery):
    checkpoint_info = Parser("kamenny_log", "cargo")
    await checkpoint_info.queue_promotion()
    try:
        await callback.message.edit_text(
            text=checkpoint_info.promotion_per_day,
            reply_markup=keyboard.ikb_kamenny_log_cargo(),
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)
