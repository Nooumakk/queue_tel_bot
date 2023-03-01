from aiogram import types
from tele_bot.bot import dp, bot
from tele_bot import keyboard
from aiogram.utils.exceptions import MessageNotModified
from tele_bot.base.parser import Parser
from tele_bot.utils.anti_flod import flood_callback
from tele_bot.middleware import _


__all__ = (
    "grigorovshcina_data",
    "back_grigorovshcina",
    "grigorovshcina_bus",
    "grigorovshcina_back_bus",
    "grigorovshcina_place_in_queue_bus",
    "grigorovshcina_queue_len_bus",
    "grigorovshcina_an_hour_bus",
    "grigorovshcina_an_day_bus",
    "grigorovshcina_passenger",
    "grigorovshcina_back_passenger",
    "grigorovshcina_place_in_queue_passenger",
    "grigorovshcina_queue_len_passenger",
    "grigorovshcina_an_hour_passenger",
    "grigorovshcina_an_day_passenger",
    "grigorovshcina_cargo",
    "grigorovshcina_back_cargo",
    "grigorovshcina_place_in_queue_cargo",
    "grigorovshcina_queue_len_cargo",
    "grigorovshcina_an_hour_cargo",
    "grigorovshcina_an_day_cargo",
)


@dp.callback_query_handler(text="grigorovshcina")
@dp.throttled(flood_callback, rate=1)
async def grigorovshcina_data(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=_("Страна: Латвия 🇱🇻\nПункт пропуска: Григоровщина"),
        reply_markup=keyboard.ikb_grigorovshcina_ts(),
    )


@dp.callback_query_handler(text="back_grigorovshcina")
@dp.throttled(flood_callback, rate=1)
async def back_grigorovshcina(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=_("Страна: Латвия 🇱🇻\nВыберите пункт пропуска"),
        reply_markup=keyboard.ikb_latvia(),
    )


@dp.callback_query_handler(text="grigorovshcina_bus")
@dp.throttled(flood_callback, rate=1)
async def grigorovshcina_bus(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=_("Страна: Латвия 🇱🇻\nПункт пропуска: Григоровщина\nТранспорт: Автобус 🚌"),
        reply_markup=keyboard.ikb_grigorovshcina_bus(),
    )


@dp.callback_query_handler(text="back_grigorovshcina_bus")
@dp.throttled(flood_callback, rate=1)
async def grigorovshcina_back_bus(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=_("Страна: Латвия 🇱🇻\nПункт пропуска: Григоровщина"),
        reply_markup=keyboard.ikb_grigorovshcina_ts(),
    )


@dp.callback_query_handler(text="grigorovshcina_place_in_queue_bus")
@dp.throttled(flood_callback, rate=1)
async def grigorovshcina_place_in_queue_bus(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    checkpoint_info = Parser("grigorovshcina", "bus")
    await checkpoint_info.get_place("bus_number", user_id)
    try:
        await callback.message.edit_text(
            text=checkpoint_info.response,
            reply_markup=keyboard.ikb_grigorovshcina_bus(),
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)
    return checkpoint_info._model


@dp.callback_query_handler(text="grigorovshcina_queue_len_bus")
@dp.throttled(flood_callback, rate=1)
async def grigorovshcina_queue_len_bus(callback: types.CallbackQuery):
    checkpoint_info = Parser("grigorovshcina", "bus")
    await checkpoint_info.len_queue()
    try:
        await callback.message.edit_text(
            text=checkpoint_info.response,
            reply_markup=keyboard.ikb_grigorovshcina_bus(),
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)


@dp.callback_query_handler(text="grigorovshcina_an_hour_bus")
@dp.throttled(flood_callback, rate=1)
async def grigorovshcina_an_hour_bus(callback: types.CallbackQuery):
    checkpoint_info = Parser("grigorovshcina", "bus")
    await checkpoint_info.queue_promotion()
    try:
        await callback.message.edit_text(
            text=checkpoint_info.promotion_per_hour,
            reply_markup=keyboard.ikb_grigorovshcina_bus(),
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)


@dp.callback_query_handler(text="grigorovshcina_an_day_bus")
@dp.throttled(flood_callback, rate=1)
async def grigorovshcina_an_day_bus(callback: types.CallbackQuery):
    checkpoint_info = Parser("grigorovshcina", "bus")
    await checkpoint_info.queue_promotion()
    try:
        await callback.message.edit_text(
            text=checkpoint_info.promotion_per_day,
            reply_markup=keyboard.ikb_grigorovshcina_bus(),
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)


@dp.callback_query_handler(text="grigorovshcina_passenger")
@dp.throttled(flood_callback, rate=1)
async def grigorovshcina_passenger(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=_(
            "Страна: Латвия 🇱🇻\nПункт пропуска: Григоровщина\nТранспорт: Легковой 🚘"
        ),
        reply_markup=keyboard.ikb_grigorovshcina_passenger(),
    )


@dp.callback_query_handler(text="back_grigorovshcina_passenger")
@dp.throttled(flood_callback, rate=1)
async def grigorovshcina_back_passenger(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=_("Страна: Латвия 🇱🇻\nПункт пропуска: Григоровщина"),
        reply_markup=keyboard.ikb_grigorovshcina_ts(),
    )


@dp.callback_query_handler(text="grigorovshcina_place_in_queue_passenger")
@dp.throttled(flood_callback, rate=1)
async def grigorovshcina_place_in_queue_passenger(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    checkpoint_info = Parser("grigorovshcina", "passenger")
    await checkpoint_info.get_place("passenger_number", user_id)
    try:
        await callback.message.edit_text(
            text=checkpoint_info.response,
            reply_markup=keyboard.ikb_grigorovshcina_passenger(),
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)
    return checkpoint_info._model


@dp.callback_query_handler(text="grigorovshcina_queue_len_passenger")
@dp.throttled(flood_callback, rate=1)
async def grigorovshcina_queue_len_passenger(callback: types.CallbackQuery):
    checkpoint_info = Parser("grigorovshcina", "passenger")
    await checkpoint_info.len_queue()
    try:
        await callback.message.edit_text(
            text=checkpoint_info.response,
            reply_markup=keyboard.ikb_grigorovshcina_passenger(),
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)


@dp.callback_query_handler(text="grigorovshcina_an_hour_passenger")
@dp.throttled(flood_callback, rate=1)
async def grigorovshcina_an_hour_passenger(callback: types.CallbackQuery):
    checkpoint_info = Parser("grigorovshcina", "passenger")
    await checkpoint_info.queue_promotion()
    try:
        await callback.message.edit_text(
            text=checkpoint_info.promotion_per_hour,
            reply_markup=keyboard.ikb_grigorovshcina_passenger(),
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)


@dp.callback_query_handler(text="grigorovshcina_an_day_passenger")
@dp.throttled(flood_callback, rate=1)
async def grigorovshcina_an_day_passenger(callback: types.CallbackQuery):
    checkpoint_info = Parser("grigorovshcina", "passenger")
    await checkpoint_info.queue_promotion()
    try:
        await callback.message.edit_text(
            text=checkpoint_info.promotion_per_day,
            reply_markup=keyboard.ikb_grigorovshcina_passenger(),
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)


@dp.callback_query_handler(text="grigorovshcina_cargo")
@dp.throttled(flood_callback, rate=1)
async def grigorovshcina_cargo(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=_(
            "Страна: Латвия 🇱🇻\nПункт пропуска: Григоровщина\nТранспорт: Грузовой  🚛"
        ),
        reply_markup=keyboard.ikb_grigorovshcina_cargo(),
    )


@dp.callback_query_handler(text="back_grigorovshcina_cargo")
@dp.throttled(flood_callback, rate=1)
async def grigorovshcina_back_cargo(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=_("Страна: Латвия 🇱🇻\nПункт пропуска: Григоровщина"),
        reply_markup=keyboard.ikb_grigorovshcina_ts(),
    )


@dp.callback_query_handler(text="grigorovshcina_place_in_queue_cargo")
@dp.throttled(flood_callback, rate=1)
async def grigorovshcina_place_in_queue_cargo(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    checkpoint_info = Parser("grigorovshcina", "cargo")
    await checkpoint_info.get_place("cargo_number", user_id)
    try:
        await callback.message.edit_text(
            text=checkpoint_info.response,
            reply_markup=keyboard.ikb_grigorovshcina_cargo(),
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)
    return checkpoint_info._model


@dp.callback_query_handler(text="grigorovshcina_queue_len_cargo")
@dp.throttled(flood_callback, rate=1)
async def grigorovshcina_queue_len_cargo(callback: types.CallbackQuery):
    checkpoint_info = Parser("grigorovshcina", "cargo")
    await checkpoint_info.len_queue()
    try:
        await callback.message.edit_text(
            text=checkpoint_info.response,
            reply_markup=keyboard.ikb_grigorovshcina_cargo(),
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)


@dp.callback_query_handler(text="grigorovshcina_an_hour_cargo")
@dp.throttled(flood_callback, rate=1)
async def grigorovshcina_an_hour_cargo(callback: types.CallbackQuery):
    checkpoint_info = Parser("grigorovshcina", "cargo")
    await checkpoint_info.queue_promotion()
    try:
        await callback.message.edit_text(
            text=checkpoint_info.promotion_per_hour,
            reply_markup=keyboard.ikb_grigorovshcina_cargo(),
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)


@dp.callback_query_handler(text="grigorovshcina_an_day_cargo")
@dp.throttled(flood_callback, rate=1)
async def grigorovshcina_an_day_cargo(callback: types.CallbackQuery):
    checkpoint_info = Parser("grigorovshcina", "cargo")
    await checkpoint_info.queue_promotion()
    try:
        await callback.message.edit_text(
            text=checkpoint_info.promotion_per_day,
            reply_markup=keyboard.ikb_grigorovshcina_cargo(),
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)
