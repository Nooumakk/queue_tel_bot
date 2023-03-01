from aiogram import types
from tele_bot.bot import dp, bot
from tele_bot import keyboard
from aiogram.utils.exceptions import MessageNotModified
from tele_bot.base.parser import Parser
from tele_bot.utils.anti_flod import flood_callback
from tele_bot.middleware import _


__all__ = (
    "kotlovka_data",
    "back_kotlovka",
    "kotlovka_bus",
    "kotlovka_back_bus",
    "kotlovka_place_in_queue_bus",
    "kotlovka_queue_len_bus",
    "kotlovka_an_hour_bus",
    "kotlovka_an_day_bus",
    "kotlovka_passenger",
    "kotlovka_back_passenger",
    "kotlovka_place_in_queue_passenger",
    "kotlovka_queue_len_passenger",
    "kotlovka_an_hour_passenger",
    "kotlovka_an_day_passenger",
    "kotlovka_cargo",
    "kotlovka_back_cargo",
    "kotlovka_place_in_queue_cargo",
    "kotlovka_queue_len_cargo",
    "kotlovka_an_hour_cargo",
    "kotlovka_an_day_cargo",
)


@dp.callback_query_handler(text="kotlovka")
@dp.throttled(flood_callback, rate=1)
async def kotlovka_data(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=_("Страна: Литва 🇱🇹\nПункт пропуска: Котловка"),
        reply_markup=keyboard.ikb_kotlovka_ts(),
    )


@dp.callback_query_handler(text="back_kotlovka")
@dp.throttled(flood_callback, rate=1)
async def back_kotlovka(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=_("Страна: Литва 🇱🇹\nВыберите пункт пропуска"),
        reply_markup=keyboard.ikb_lithuania(),
    )


@dp.callback_query_handler(text="kotlovka_bus")
@dp.throttled(flood_callback, rate=1)
async def kotlovka_bus(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=_("Страна: Литва 🇱🇹\nПункт пропуска: Котловка\nТранспорт: Автобус 🚌"),
        reply_markup=keyboard.ikb_kotlovka_bus(),
    )


@dp.callback_query_handler(text="back_kotlovka_bus")
@dp.throttled(flood_callback, rate=1)
async def kotlovka_back_bus(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=_("Страна: Литва 🇱🇹\nПункт пропуска: Котловка"),
        reply_markup=keyboard.ikb_kotlovka_ts(),
    )


@dp.callback_query_handler(text="kotlovka_place_in_queue_bus")
@dp.throttled(flood_callback, rate=1)
async def kotlovka_place_in_queue_bus(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    checkpoint_info = Parser("kotlovka", "bus")
    await checkpoint_info.get_place("bus_number", user_id)
    try:
        await callback.message.edit_text(
            text=checkpoint_info.response, reply_markup=keyboard.ikb_kotlovka_bus()
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)
    return checkpoint_info._model


@dp.callback_query_handler(text="kotlovka_queue_len_bus")
@dp.throttled(flood_callback, rate=1)
async def kotlovka_queue_len_bus(callback: types.CallbackQuery):
    checkpoint_info = Parser("kotlovka", "bus")
    await checkpoint_info.len_queue()
    try:
        await callback.message.edit_text(
            text=checkpoint_info.response, reply_markup=keyboard.ikb_kotlovka_bus()
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)


@dp.callback_query_handler(text="kotlovka_an_hour_bus")
@dp.throttled(flood_callback, rate=1)
async def kotlovka_an_hour_bus(callback: types.CallbackQuery):
    checkpoint_info = Parser("kotlovka", "bus")
    await checkpoint_info.queue_promotion()
    try:
        await callback.message.edit_text(
            text=checkpoint_info.promotion_per_hour,
            reply_markup=keyboard.ikb_kotlovka_bus(),
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)


@dp.callback_query_handler(text="kotlovka_an_day_bus")
@dp.throttled(flood_callback, rate=1)
async def kotlovka_an_day_bus(callback: types.CallbackQuery):
    checkpoint_info = Parser("kotlovka", "bus")
    await checkpoint_info.queue_promotion()
    try:
        await callback.message.edit_text(
            text=checkpoint_info.promotion_per_day,
            reply_markup=keyboard.ikb_kotlovka_bus(),
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)


@dp.callback_query_handler(text="kotlovka_passenger")
@dp.throttled(flood_callback, rate=1)
async def kotlovka_passenger(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=_("Страна: Литва 🇱🇹\nПункт пропуска: Котловка\nТранспорт: Легковой 🚘"),
        reply_markup=keyboard.ikb_kotlovka_passenger(),
    )


@dp.callback_query_handler(text="back_kotlovka_passenger")
@dp.throttled(flood_callback, rate=1)
async def kotlovka_back_passenger(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=_("Страна: Литва 🇱🇹\nПункт пропуска: Котловка"),
        reply_markup=keyboard.ikb_kotlovka_ts(),
    )


@dp.callback_query_handler(text="kotlovka_place_in_queue_passenger")
@dp.throttled(flood_callback, rate=1)
async def kotlovka_place_in_queue_passenger(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    checkpoint_info = Parser("kotlovka", "passenger")
    await checkpoint_info.get_place("passenger_number", user_id)
    try:
        await callback.message.edit_text(
            text=checkpoint_info.response,
            reply_markup=keyboard.ikb_kotlovka_passenger(),
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)
    return checkpoint_info._model


@dp.callback_query_handler(text="kotlovka_queue_len_passenger")
@dp.throttled(flood_callback, rate=1)
async def kotlovka_queue_len_passenger(callback: types.CallbackQuery):
    checkpoint_info = Parser("kotlovka", "passenger")
    await checkpoint_info.len_queue()
    try:
        await callback.message.edit_text(
            text=checkpoint_info.response,
            reply_markup=keyboard.ikb_kotlovka_passenger(),
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)


@dp.callback_query_handler(text="kotlovka_an_hour_passenger")
@dp.throttled(flood_callback, rate=1)
async def kotlovka_an_hour_passenger(callback: types.CallbackQuery):
    checkpoint_info = Parser("kotlovka", "passenger")
    await checkpoint_info.queue_promotion()
    try:
        await callback.message.edit_text(
            text=checkpoint_info.promotion_per_hour,
            reply_markup=keyboard.ikb_kotlovka_passenger(),
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)


@dp.callback_query_handler(text="kotlovka_an_day_passenger")
@dp.throttled(flood_callback, rate=1)
async def kotlovka_an_day_passenger(callback: types.CallbackQuery):
    checkpoint_info = Parser("kotlovka", "passenger")
    await checkpoint_info.queue_promotion()
    try:
        await callback.message.edit_text(
            text=checkpoint_info.promotion_per_day,
            reply_markup=keyboard.ikb_kotlovka_passenger(),
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)


@dp.callback_query_handler(text="kotlovka_cargo")
@dp.throttled(flood_callback, rate=1)
async def kotlovka_cargo(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=_("Страна: Литва 🇱🇹\nПункт пропуска: Котловка\nТранспорт: Грузовой  🚛"),
        reply_markup=keyboard.ikb_kotlovka_cargo(),
    )


@dp.callback_query_handler(text="back_kotlovka_cargo")
@dp.throttled(flood_callback, rate=1)
async def kotlovka_back_cargo(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=_("Страна: Литва 🇱🇹\nПункт пропуска: Котловка"),
        reply_markup=keyboard.ikb_kotlovka_ts(),
    )


@dp.callback_query_handler(text="kotlovka_place_in_queue_cargo")
@dp.throttled(flood_callback, rate=1)
async def kotlovka_place_in_queue_cargo(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    checkpoint_info = Parser("kotlovka", "cargo")
    await checkpoint_info.get_place("cargo_number", user_id)
    try:
        await callback.message.edit_text(
            text=checkpoint_info.response, reply_markup=keyboard.ikb_kotlovka_cargo()
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)
    return checkpoint_info._model


@dp.callback_query_handler(text="kotlovka_queue_len_cargo")
@dp.throttled(flood_callback, rate=1)
async def kotlovka_queue_len_cargo(callback: types.CallbackQuery):
    checkpoint_info = Parser("kotlovka", "cargo")
    await checkpoint_info.len_queue()
    try:
        await callback.message.edit_text(
            text=checkpoint_info.response, reply_markup=keyboard.ikb_kotlovka_cargo()
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)


@dp.callback_query_handler(text="kotlovka_an_hour_cargo")
@dp.throttled(flood_callback, rate=1)
async def kotlovka_an_hour_cargo(callback: types.CallbackQuery):
    checkpoint_info = Parser("kotlovka", "cargo")
    await checkpoint_info.queue_promotion()
    try:
        await callback.message.edit_text(
            text=checkpoint_info.promotion_per_hour,
            reply_markup=keyboard.ikb_kotlovka_cargo(),
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)


@dp.callback_query_handler(text="kotlovka_an_day_cargo")
@dp.throttled(flood_callback, rate=1)
async def kotlovka_an_day_cargo(callback: types.CallbackQuery):
    checkpoint_info = Parser("kotlovka", "cargo")
    await checkpoint_info.queue_promotion()
    try:
        await callback.message.edit_text(
            text=checkpoint_info.promotion_per_day,
            reply_markup=keyboard.ikb_kotlovka_cargo(),
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)
