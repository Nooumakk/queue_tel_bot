from aiogram import types
from tele_bot.bot import dp, bot
from tele_bot import keyboard
from aiogram.utils.exceptions import MessageNotModified
from tele_bot.base.parser import Parser
from tele_bot.utils.anti_flod import flood_callback
from tele_bot.middleware import _


__all__ = (
    "urbany_data",
    "back_urbany",
    "urbany_bus",
    "urbany_back_bus",
    "urbany_place_in_queue_bus",
    "urbany_queue_len_bus",
    "urbany_an_hour_bus",
    "urbany_an_day_bus",
    "urbany_passenger",
    "urbany_back_passenger",
    "urbany_place_in_queue_passenger",
    "urbany_queue_len_passenger",
    "urbany_an_hour_passenger",
    "urbany_an_day_passenger",
    "urbany_cargo",
    "urbany_back_cargo",
    "urbany_place_in_queue_cargo",
    "urbany_queue_len_cargo",
    "urbany_an_hour_cargo",
    "urbany_an_day_cargo",
)


@dp.callback_query_handler(text="urbany")
@dp.throttled(flood_callback, rate=1)
async def urbany_data(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=_("Страна: Латвия 🇱🇻\nПункт пропуска: Урбаны"),
        reply_markup=keyboard.ikb_urbany_ts(),
    )


@dp.callback_query_handler(text="back_urbany")
@dp.throttled(flood_callback, rate=1)
async def back_urbany(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=_("Страна: Латвия 🇱🇻\nВыберите пункт пропуска"),
        reply_markup=keyboard.ikb_latvia(),
    )


@dp.callback_query_handler(text="urbany_bus")
@dp.throttled(flood_callback, rate=1)
async def urbany_bus(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=_("Страна: Латвия 🇱🇻\nПункт пропуска: Урбаны\nТранспорт: Автобус 🚌"),
        reply_markup=keyboard.ikb_urbany_bus(),
    )


@dp.callback_query_handler(text="back_urbany_bus")
@dp.throttled(flood_callback, rate=1)
async def urbany_back_bus(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=_("Страна: Латвия 🇱🇻\nПункт пропуска: Урбаны"),
        reply_markup=keyboard.ikb_urbany_ts(),
    )


@dp.callback_query_handler(text="urbany_place_in_queue_bus")
@dp.throttled(flood_callback, rate=1)
async def urbany_place_in_queue_bus(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    checkpoint_info = Parser("urbany", "bus")
    await checkpoint_info.get_place("bus_number", user_id)
    try:
        await callback.message.edit_text(
            text=checkpoint_info.response, reply_markup=keyboard.ikb_urbany_bus()
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)
    return checkpoint_info._model


@dp.callback_query_handler(text="urbany_queue_len_bus")
@dp.throttled(flood_callback, rate=1)
async def urbany_queue_len_bus(callback: types.CallbackQuery):
    checkpoint_info = Parser("urbany", "bus")
    await checkpoint_info.len_queue()
    try:
        await callback.message.edit_text(
            text=checkpoint_info.response, reply_markup=keyboard.ikb_urbany_bus()
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)


@dp.callback_query_handler(text="urbany_an_hour_bus")
@dp.throttled(flood_callback, rate=1)
async def urbany_an_hour_bus(callback: types.CallbackQuery):
    checkpoint_info = Parser("urbany", "bus")
    await checkpoint_info.queue_promotion()
    try:
        await callback.message.edit_text(
            text=checkpoint_info.promotion_per_hour,
            reply_markup=keyboard.ikb_urbany_bus(),
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)


@dp.callback_query_handler(text="urbany_an_day_bus")
@dp.throttled(flood_callback, rate=1)
async def urbany_an_day_bus(callback: types.CallbackQuery):
    checkpoint_info = Parser("urbany", "bus")
    await checkpoint_info.queue_promotion()
    try:
        await callback.message.edit_text(
            text=checkpoint_info.promotion_per_day,
            reply_markup=keyboard.ikb_urbany_bus(),
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)


@dp.callback_query_handler(text="urbany_passenger")
@dp.throttled(flood_callback, rate=1)
async def urbany_passenger(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=_("Страна: Латвия 🇱🇻\nПункт пропуска: Урбаны\nТранспорт: Легковой 🚘"),
        reply_markup=keyboard.ikb_urbany_passenger(),
    )


@dp.callback_query_handler(text="back_urbany_passenger")
@dp.throttled(flood_callback, rate=1)
async def urbany_back_passenger(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=_("Страна: Латвия 🇱🇻\nПункт пропуска: Урбаны"),
        reply_markup=keyboard.ikb_urbany_ts(),
    )


@dp.callback_query_handler(text="urbany_place_in_queue_passenger")
@dp.throttled(flood_callback, rate=1)
async def urbany_place_in_queue_passenger(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    checkpoint_info = Parser("urbany", "passenger")
    await checkpoint_info.get_place("passenger_number", user_id)
    try:
        await callback.message.edit_text(
            text=checkpoint_info.response, reply_markup=keyboard.ikb_urbany_passenger()
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)
    return checkpoint_info._model


@dp.callback_query_handler(text="urbany_queue_len_passenger")
@dp.throttled(flood_callback, rate=1)
async def urbany_queue_len_passenger(callback: types.CallbackQuery):
    checkpoint_info = Parser("urbany", "passenger")
    await checkpoint_info.len_queue()
    try:
        await callback.message.edit_text(
            text=checkpoint_info.response, reply_markup=keyboard.ikb_urbany_passenger()
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)


@dp.callback_query_handler(text="urbany_an_hour_passenger")
@dp.throttled(flood_callback, rate=1)
async def urbany_an_hour_passenger(callback: types.CallbackQuery):
    checkpoint_info = Parser("urbany", "passenger")
    await checkpoint_info.queue_promotion()
    try:
        await callback.message.edit_text(
            text=checkpoint_info.promotion_per_hour,
            reply_markup=keyboard.ikb_urbany_passenger(),
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)


@dp.callback_query_handler(text="urbany_an_day_passenger")
@dp.throttled(flood_callback, rate=1)
async def urbany_an_day_passenger(callback: types.CallbackQuery):
    checkpoint_info = Parser("urbany", "passenger")
    await checkpoint_info.queue_promotion()
    try:
        await callback.message.edit_text(
            text=checkpoint_info.promotion_per_day,
            reply_markup=keyboard.ikb_urbany_passenger(),
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)


@dp.callback_query_handler(text="urbany_cargo")
@dp.throttled(flood_callback, rate=1)
async def urbany_cargo(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=_("Страна: Латвия 🇱🇻\nПункт пропуска: Урбаны\nТранспорт: Грузовой  🚛"),
        reply_markup=keyboard.ikb_urbany_cargo(),
    )


@dp.callback_query_handler(text="back_urbany_cargo")
@dp.throttled(flood_callback, rate=1)
async def urbany_back_cargo(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=_("Страна: Латвия 🇱🇻\nПункт пропуска: Урбаны"),
        reply_markup=keyboard.ikb_urbany_ts(),
    )


@dp.callback_query_handler(text="urbany_place_in_queue_cargo")
@dp.throttled(flood_callback, rate=1)
async def urbany_place_in_queue_cargo(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    checkpoint_info = Parser("urbany", "cargo")
    await checkpoint_info.get_place("cargo_number", user_id)
    try:
        await callback.message.edit_text(
            text=checkpoint_info.response, reply_markup=keyboard.ikb_urbany_cargo()
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)
    return checkpoint_info._model


@dp.callback_query_handler(text="urbany_queue_len_cargo")
@dp.throttled(flood_callback, rate=1)
async def urbany_queue_len_cargo(callback: types.CallbackQuery):
    checkpoint_info = Parser("urbany", "cargo")
    await checkpoint_info.len_queue()
    try:
        await callback.message.edit_text(
            text=checkpoint_info.response, reply_markup=keyboard.ikb_urbany_cargo()
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)


@dp.callback_query_handler(text="urbany_an_hour_cargo")
@dp.throttled(flood_callback, rate=1)
async def urbany_an_hour_cargo(callback: types.CallbackQuery):
    checkpoint_info = Parser("urbany", "cargo")
    await checkpoint_info.queue_promotion()
    try:
        await callback.message.edit_text(
            text=checkpoint_info.promotion_per_hour,
            reply_markup=keyboard.ikb_urbany_cargo(),
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)


@dp.callback_query_handler(text="urbany_an_day_cargo")
@dp.throttled(flood_callback, rate=1)
async def urbany_an_day_cargo(callback: types.CallbackQuery):
    checkpoint_info = Parser("urbany", "cargo")
    await checkpoint_info.queue_promotion()
    try:
        await callback.message.edit_text(
            text=checkpoint_info.promotion_per_day,
            reply_markup=keyboard.ikb_urbany_cargo(),
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)
