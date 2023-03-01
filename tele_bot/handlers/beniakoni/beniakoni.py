from aiogram import types
from tele_bot.bot import dp, bot
from tele_bot import keyboard
from aiogram.utils.exceptions import MessageNotModified
from tele_bot.base.parser import Parser
from tele_bot.utils.anti_flod import flood_callback
from tele_bot.middleware import _


__all__ = (
    "beniakoni_data",
    "back_beniakoni",
    "beniakoni_bus",
    "beniakoni_back_bus",
    "beniakoni_place_in_queue_bus",
    "beniakoni_queue_len_bus",
    "beniakoni_an_hour_bus",
    "beniakoni_an_day_bus",
    "beniakoni_passenger",
    "beniakoni_back_passenger",
    "beniakoni_place_in_queue_passenger",
    "beniakoni_queue_len_passenger",
    "beniakoni_an_hour_passenger",
    "beniakoni_an_day_passenger",
    "beniakoni_cargo",
    "beniakoni_back_cargo",
    "beniakoni_place_in_queue_cargo",
    "beniakoni_queue_len_cargo",
    "beniakoni_an_hour_cargo",
    "beniakoni_an_day_cargo",
)


@dp.callback_query_handler(text="beniakoni")
@dp.throttled(flood_callback, rate=1)
async def beniakoni_data(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=_("Страна: Литва 🇱🇹\nПункт пропуска: Бенякони"),
        reply_markup=keyboard.ikb_beniakoni_ts(),
    )


@dp.callback_query_handler(text="back_beniakoni")
@dp.throttled(flood_callback, rate=1)
async def back_beniakoni(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=_("Страна: Литва 🇱🇹\nВыберите пункт пропуска"),
        reply_markup=keyboard.ikb_lithuania(),
    )


@dp.callback_query_handler(text="beniakoni_bus")
@dp.throttled(flood_callback, rate=1)
async def beniakoni_bus(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=_("Страна: Литва 🇱🇹\nПункт пропуска: Бенякони\nТранспорт: Автобус 🚌"),
        reply_markup=keyboard.ikb_beniakoni_bus(),
    )


@dp.callback_query_handler(text="back_beniakoni_bus")
@dp.throttled(flood_callback, rate=1)
async def beniakoni_back_bus(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=_("Страна: Литва 🇱🇹\nПункт пропуска: Бенякони"),
        reply_markup=keyboard.ikb_beniakoni_ts(),
    )


@dp.callback_query_handler(text="beniakoni_place_in_queue_bus")
@dp.throttled(flood_callback, rate=1)
async def beniakoni_place_in_queue_bus(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    checkpoint_info = Parser("beniakoni", "bus")
    await checkpoint_info.get_place("bus_number", user_id)
    try:
        await callback.message.edit_text(
            text=checkpoint_info.response, reply_markup=keyboard.ikb_beniakoni_bus()
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)
    return checkpoint_info._model


@dp.callback_query_handler(text="beniakoni_queue_len_bus")
@dp.throttled(flood_callback, rate=1)
async def beniakoni_queue_len_bus(callback: types.CallbackQuery):
    checkpoint_info = Parser("beniakoni", "bus")
    await checkpoint_info.len_queue()
    try:
        await callback.message.edit_text(
            text=checkpoint_info.response, reply_markup=keyboard.ikb_beniakoni_bus()
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)


@dp.callback_query_handler(text="beniakoni_an_hour_bus")
@dp.throttled(flood_callback, rate=1)
async def beniakoni_an_hour_bus(callback: types.CallbackQuery):
    try:
        checkpoint_info = Parser("beniakoni", "bus")
        await checkpoint_info.queue_promotion()
        await callback.message.edit_text(
            text=checkpoint_info.promotion_per_hour,
            reply_markup=keyboard.ikb_beniakoni_bus(),
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)


@dp.callback_query_handler(text="beniakoni_an_day_bus")
@dp.throttled(flood_callback, rate=1)
async def beniakoni_an_day_bus(callback: types.CallbackQuery):
    try:
        checkpoint_info = Parser("beniakoni", "bus")
        await checkpoint_info.queue_promotion()
        await callback.message.edit_text(
            text=checkpoint_info.promotion_per_day,
            reply_markup=keyboard.ikb_beniakoni_bus(),
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)


@dp.callback_query_handler(text="beniakoni_passenger")
@dp.throttled(flood_callback, rate=1)
async def beniakoni_passenger(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=_("Страна: Литва 🇱🇹\nПункт пропуска: Бенякони\nТранспорт: Легковой 🚘"),
        reply_markup=keyboard.ikb_beniakoni_passenger(),
    )


@dp.callback_query_handler(text="back_beniakoni_passenger")
@dp.throttled(flood_callback, rate=1)
async def beniakoni_back_passenger(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=_("Страна: Литва 🇱🇹\nПункт пропуска: Бенякони"),
        reply_markup=keyboard.ikb_beniakoni_ts(),
    )


@dp.callback_query_handler(text="beniakoni_place_in_queue_passenger")
@dp.throttled(flood_callback, rate=1)
async def beniakoni_place_in_queue_passenger(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    checkpoint_info = Parser("beniakoni", "passenger")
    await checkpoint_info.get_place("passenger_number", user_id)
    try:
        await callback.message.edit_text(
            text=checkpoint_info.response,
            reply_markup=keyboard.ikb_beniakoni_passenger(),
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)
    return checkpoint_info._model


@dp.callback_query_handler(text="beniakoni_queue_len_passenger")
@dp.throttled(flood_callback, rate=1)
async def beniakoni_queue_len_passenger(callback: types.CallbackQuery):
    checkpoint_info = Parser("beniakoni", "passenger")
    await checkpoint_info.len_queue()
    try:
        await callback.message.edit_text(
            text=checkpoint_info.response,
            reply_markup=keyboard.ikb_beniakoni_passenger(),
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)


@dp.callback_query_handler(text="beniakoni_an_hour_passenger")
@dp.throttled(flood_callback, rate=1)
async def beniakoni_an_hour_passenger(callback: types.CallbackQuery):
    checkpoint_info = Parser("beniakoni", "passenger")
    await checkpoint_info.queue_promotion()
    try:
        await callback.message.edit_text(
            text=checkpoint_info.promotion_per_hour,
            reply_markup=keyboard.ikb_beniakoni_passenger(),
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)


@dp.callback_query_handler(text="beniakoni_an_day_passenger")
@dp.throttled(flood_callback, rate=1)
async def beniakoni_an_day_passenger(callback: types.CallbackQuery):
    checkpoint_info = Parser("beniakoni", "passenger")
    await checkpoint_info.queue_promotion()
    try:
        await callback.message.edit_text(
            text=checkpoint_info.promotion_per_day,
            reply_markup=keyboard.ikb_beniakoni_passenger(),
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)


@dp.callback_query_handler(text="beniakoni_cargo")
@dp.throttled(flood_callback, rate=1)
async def beniakoni_cargo(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=_("Страна: Литва 🇱🇹\nПункт пропуска: Бенякони\nТранспорт: Грузовой  🚛"),
        reply_markup=keyboard.ikb_beniakoni_cargo(),
    )


@dp.callback_query_handler(text="back_beniakoni_cargo")
@dp.throttled(flood_callback, rate=1)
async def beniakoni_back_cargo(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=_("Страна: Литва 🇱🇹\nПункт пропуска: Бенякони"),
        reply_markup=keyboard.ikb_beniakoni_ts(),
    )


@dp.callback_query_handler(text="beniakoni_place_in_queue_cargo")
@dp.throttled(flood_callback, rate=1)
async def beniakoni_place_in_queue_cargo(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    checkpoint_info = Parser("beniakoni", "cargo")
    await checkpoint_info.get_place("cargo_number", user_id)
    try:
        await callback.message.edit_text(
            text=checkpoint_info.response, reply_markup=keyboard.ikb_beniakoni_cargo()
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)
    return checkpoint_info._model


@dp.callback_query_handler(text="beniakoni_queue_len_cargo")
@dp.throttled(flood_callback, rate=1)
async def beniakoni_queue_len_cargo(callback: types.CallbackQuery):
    checkpoint_info = Parser("beniakoni", "cargo")
    await checkpoint_info.len_queue()
    try:
        await callback.message.edit_text(
            text=checkpoint_info.response, reply_markup=keyboard.ikb_beniakoni_cargo()
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)


@dp.callback_query_handler(text="beniakoni_an_hour_cargo")
@dp.throttled(flood_callback, rate=1)
async def beniakoni_an_hour_cargo(callback: types.CallbackQuery):
    checkpoint_info = Parser("beniakoni", "cargo")
    await checkpoint_info.queue_promotion()
    try:
        await callback.message.edit_text(
            text=checkpoint_info.promotion_per_hour,
            reply_markup=keyboard.ikb_beniakoni_cargo(),
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)


@dp.callback_query_handler(text="beniakoni_an_day_cargo")
@dp.throttled(flood_callback, rate=1)
async def beniakoni_an_day_cargo(callback: types.CallbackQuery):
    checkpoint_info = Parser("beniakoni", "cargo")
    await checkpoint_info.queue_promotion()
    try:
        await callback.message.edit_text(
            text=checkpoint_info.promotion_per_day,
            reply_markup=keyboard.ikb_beniakoni_cargo(),
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)
