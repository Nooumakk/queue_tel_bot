from aiogram import types
from tele_bot.bot import dp, bot
from tele_bot import keyboard
from aiogram.utils.exceptions import MessageNotModified
from tele_bot.base.parser import Parser
from tele_bot.utils.anti_flod import flood_callback
from tele_bot.middleware import _


__all__ = (
    "brest_data",
    "back_brest",
    "brest_bus",
    "brest_back_bus",
    "brest_place_in_queue_bus",
    "brest_queue_len_bus",
    "brest_an_hour_bus",
    "brest_an_day_bus",
    "brest_passenger",
    "brest_back_passenger",
    "brest_place_in_queue_passenger",
    "brest_queue_len_passenger",
    "brest_an_hour_passenger",
    "brest_an_day_passenger",
    "brest_cargo",
    "brest_back_cargo",
    "brest_place_in_queue_cargo",
    "brest_queue_len_cargo",
    "brest_an_hour_cargo",
    "brest_an_day_cargo",
)


@dp.callback_query_handler(text="brest")
@dp.throttled(flood_callback, rate=1)
async def brest_data(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=_("Страна: Польша 🇵🇱\nПункт пропуска: Брест"),
        reply_markup=keyboard.ikb_brest_ts(),
    )


@dp.callback_query_handler(text="back_brest")
@dp.throttled(flood_callback, rate=1)
async def back_brest(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=_("Страна: Польша 🇵🇱\nВыберите пункт пропуска"),
        reply_markup=keyboard.ikb_poland(),
    )


@dp.callback_query_handler(text="brest_bus")
@dp.throttled(flood_callback, rate=1)
async def brest_bus(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=_("Страна: Польша 🇵🇱\nПункт пропуска: Брест\nТранспорт: Автобус 🚌"),
        reply_markup=keyboard.ikb_brest_bus(),
    )


@dp.callback_query_handler(text="back_brest_bus")
@dp.throttled(flood_callback, rate=1)
async def brest_back_bus(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=_("Страна: Польша 🇵🇱\nПункт пропуска: Брест"),
        reply_markup=keyboard.ikb_brest_ts(),
    )


@dp.callback_query_handler(text="brest_place_in_queue_bus")
@dp.throttled(flood_callback, rate=1)
async def brest_place_in_queue_bus(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    checkpoint_info = Parser("brest", "bus")
    await checkpoint_info.get_place("bus_number", user_id)
    try:
        await callback.message.edit_text(
            text=checkpoint_info.response, reply_markup=keyboard.ikb_brest_bus()
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)
    return checkpoint_info._model


@dp.callback_query_handler(text="brest_queue_len_bus")
@dp.throttled(flood_callback, rate=1)
async def brest_queue_len_bus(callback: types.CallbackQuery):
    checkpoint_info = Parser("brest", "bus")
    await checkpoint_info.len_queue()
    try:
        await callback.message.edit_text(
            text=checkpoint_info.response, reply_markup=keyboard.ikb_brest_bus()
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)


@dp.callback_query_handler(text="brest_an_hour_bus")
@dp.throttled(flood_callback, rate=1)
async def brest_an_hour_bus(callback: types.CallbackQuery):
    checkpoint_info = Parser("brest", "bus")
    await checkpoint_info.queue_promotion()
    try:
        await callback.message.edit_text(
            text=checkpoint_info.promotion_per_hour,
            reply_markup=keyboard.ikb_brest_bus(),
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)


@dp.callback_query_handler(text="brest_an_day_bus")
@dp.throttled(flood_callback, rate=1)
async def brest_an_day_bus(callback: types.CallbackQuery):
    checkpoint_info = Parser("brest", "bus")
    await checkpoint_info.queue_promotion()
    try:
        await callback.message.edit_text(
            text=checkpoint_info.promotion_per_day,
            reply_markup=keyboard.ikb_brest_bus(),
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)


@dp.callback_query_handler(text="brest_passenger")
@dp.throttled(flood_callback, rate=1)
async def brest_passenger(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=_("Страна: Польша 🇵🇱\nПункт пропуска: Брест\nТранспорт: Легковой 🚘"),
        reply_markup=keyboard.ikb_brest_passenger(),
    )


@dp.callback_query_handler(text="back_brest_passenger")
@dp.throttled(flood_callback, rate=1)
async def brest_back_passenger(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=_("Страна: Польша 🇵🇱\nПункт пропуска: Брест"),
        reply_markup=keyboard.ikb_brest_ts(),
    )


@dp.callback_query_handler(text="brest_place_in_queue_passenger")
@dp.throttled(flood_callback, rate=1)
async def brest_place_in_queue_passenger(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    checkpoint_info = Parser("brest", "passenger")
    await checkpoint_info.get_place("passenger_number", user_id)
    try:
        await callback.message.edit_text(
            text=checkpoint_info.response, reply_markup=keyboard.ikb_brest_passenger()
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)
    return checkpoint_info._model


@dp.callback_query_handler(text="brest_queue_len_passenger")
@dp.throttled(flood_callback, rate=1)
async def brest_queue_len_passenger(callback: types.CallbackQuery):
    checkpoint_info = Parser("brest", "passenger")
    await checkpoint_info.len_queue()
    try:
        await callback.message.edit_text(
            text=checkpoint_info.response, reply_markup=keyboard.ikb_brest_passenger()
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)


@dp.callback_query_handler(text="brest_an_hour_passenger")
@dp.throttled(flood_callback, rate=1)
async def brest_an_hour_passenger(callback: types.CallbackQuery):
    checkpoint_info = Parser("brest", "passenger")
    await checkpoint_info.queue_promotion()
    try:
        await callback.message.edit_text(
            text=checkpoint_info.promotion_per_hour,
            reply_markup=keyboard.ikb_brest_passenger(),
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)


@dp.callback_query_handler(text="brest_an_day_passenger")
@dp.throttled(flood_callback, rate=1)
async def brest_an_day_passenger(callback: types.CallbackQuery):
    checkpoint_info = Parser("brest", "passenger")
    await checkpoint_info.queue_promotion()
    try:
        await callback.message.edit_text(
            text=checkpoint_info.promotion_per_day,
            reply_markup=keyboard.ikb_brest_passenger(),
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)


@dp.callback_query_handler(text="brest_cargo")
@dp.throttled(flood_callback, rate=1)
async def brest_cargo(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=_("Страна: Польша 🇵🇱\nПункт пропуска: Брест\nТранспорт: Грузовой  🚛"),
        reply_markup=keyboard.ikb_brest_cargo(),
    )


@dp.callback_query_handler(text="back_brest_cargo")
@dp.throttled(flood_callback, rate=1)
async def brest_back_cargo(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=_("Страна: Польша 🇵🇱\nПункт пропуска: Брест"),
        reply_markup=keyboard.ikb_brest_ts(),
    )


@dp.callback_query_handler(text="brest_place_in_queue_cargo")
@dp.throttled(flood_callback, rate=1)
async def brest_place_in_queue_cargo(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    checkpoint_info = Parser("brest", "cargo")
    await checkpoint_info.get_place("cargo_number", user_id)
    try:
        await callback.message.edit_text(
            text=checkpoint_info.response, reply_markup=keyboard.ikb_brest_cargo()
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)
    return checkpoint_info._model


@dp.callback_query_handler(text="brest_queue_len_cargo")
@dp.throttled(flood_callback, rate=1)
async def brest_queue_len_cargo(callback: types.CallbackQuery):
    checkpoint_info = Parser("brest", "cargo")
    await checkpoint_info.len_queue()
    try:
        await callback.message.edit_text(
            text=checkpoint_info.response, reply_markup=keyboard.ikb_brest_cargo()
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)


@dp.callback_query_handler(text="brest_an_hour_cargo")
@dp.throttled(flood_callback, rate=1)
async def brest_an_hour_cargo(callback: types.CallbackQuery):
    checkpoint_info = Parser("brest", "cargo")
    await checkpoint_info.queue_promotion()
    try:
        await callback.message.edit_text(
            text=checkpoint_info.promotion_per_hour,
            reply_markup=keyboard.ikb_brest_cargo(),
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)


@dp.callback_query_handler(text="brest_an_day_cargo")
@dp.throttled(flood_callback, rate=1)
async def brest_an_day_cargo(callback: types.CallbackQuery):
    checkpoint_info = Parser("brest", "cargo")
    await checkpoint_info.queue_promotion()
    try:
        await callback.message.edit_text(
            text=checkpoint_info.promotion_per_day,
            reply_markup=keyboard.ikb_brest_cargo(),
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)
