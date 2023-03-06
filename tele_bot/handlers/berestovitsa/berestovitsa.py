from aiogram import types
from tele_bot.bot import dp, bot
from tele_bot import keyboard
from aiogram.utils.exceptions import MessageNotModified
from tele_bot.base.parser import Parser
from tele_bot.utils.anti_flod import flood_callback
from tele_bot.middleware import _


@dp.callback_query_handler(text="berestovitsa")
@dp.throttled(flood_callback, rate=1)
async def berestovitsa_data(callback: types.CallbackQuery):
    try:
        await callback.message.edit_text(
            text=_(
                "С 10.02.2023 пункт пропуска 'Берестовица' закрыт на неопределенный срок"
            ),
            reply_markup=keyboard.ikb_poland(),
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)


@dp.callback_query_handler(text="back_berestovitsa")
@dp.throttled(flood_callback, rate=1)
async def back_berestovitsa(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=_("Страна: Польша 🇵🇱\nВыберите пункт пропуска"),
        reply_markup=keyboard.ikb_poland(),
    )


@dp.callback_query_handler(text="berestovitsa_bus")
@dp.throttled(flood_callback, rate=1)
async def berestovitsa_bus(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=_("Страна: Польша 🇵🇱\nПункт пропуска: Берестовица\nТранспорт: Автобус 🚌"),
        reply_markup=keyboard.ikb_berestovitsa_bus(),
    )


@dp.callback_query_handler(text="back_berestovitsa_bus")
@dp.throttled(flood_callback, rate=1)
async def berestovitsa_back_bus(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=_("Страна: Польша 🇵🇱\nПункт пропуска: Берестовица"),
        reply_markup=keyboard.ikb_berestovitsa_ts(),
    )


@dp.callback_query_handler(text="berestovitsa_place_in_queue_bus")
@dp.throttled(flood_callback, rate=1)
async def berestovitsa_place_in_queue_bus(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    checkpoint_info = Parser("berestovica", user_id=user_id, transport="bus")
    await checkpoint_info.get_place()
    try:
        await callback.message.edit_text(
            text=checkpoint_info.response, reply_markup=keyboard.ikb_berestovitsa_bus()
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)
    return checkpoint_info._model


@dp.callback_query_handler(text="berestovitsa_queue_len_bus")
@dp.throttled(flood_callback, rate=1)
async def berestovitsa_queue_len_bus(callback: types.CallbackQuery):
    checkpoint_info = Parser("checkpoint", checkpoint="Берестовица", transport="Bus")
    await checkpoint_info.len_queue()
    try:
        await callback.message.edit_text(
            text=checkpoint_info.response, reply_markup=keyboard.ikb_berestovitsa_bus()
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)


@dp.callback_query_handler(text="berestovitsa_an_hour_bus")
@dp.throttled(flood_callback, rate=1)
async def berestovitsa_an_hour_bus(callback: types.CallbackQuery):
    checkpoint_info = Parser("stat7", transport="bus")
    await checkpoint_info.queue_promotion_per_hour()
    try:
        await callback.message.edit_text(
            text=checkpoint_info.response,
            reply_markup=keyboard.ikb_berestovitsa_bus(),
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)


@dp.callback_query_handler(text="berestovitsa_an_day_bus")
@dp.throttled(flood_callback, rate=1)
async def berestovitsa_an_day_bus(callback: types.CallbackQuery):
    checkpoint_info = Parser("stat7", transport="bus")
    await checkpoint_info.queue_promotion_per_day()
    try:
        await callback.message.edit_text(
            text=checkpoint_info.response,
            reply_markup=keyboard.ikb_berestovitsa_bus(),
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)


@dp.callback_query_handler(text="berestovitsa_passenger")
@dp.throttled(flood_callback, rate=1)
async def berestovitsa_passenger(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=_("Страна: Польша 🇵🇱\nПункт пропуска: Берестовица\nТранспорт: Легковой 🚘"),
        reply_markup=keyboard.ikb_berestovitsa_passenger(),
    )


@dp.callback_query_handler(text="back_berestovitsa_passenger")
@dp.throttled(flood_callback, rate=1)
async def berestovitsa_back_passenger(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=_("Страна: Польша 🇵🇱\nПункт пропуска: Берестовица"),
        reply_markup=keyboard.ikb_berestovitsa_ts(),
    )


@dp.callback_query_handler(text="berestovitsa_place_in_queue_passenger")
@dp.throttled(flood_callback, rate=1)
async def berestovitsa_place_in_queue_passenger(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    checkpoint_info = Parser("berestovica", user_id=user_id, transport="car")
    await checkpoint_info.get_place()
    try:
        await callback.message.edit_text(
            text=checkpoint_info.response,
            reply_markup=keyboard.ikb_berestovitsa_passenger(),
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)
    return checkpoint_info._model


@dp.callback_query_handler(text="berestovitsa_queue_len_passenger")
@dp.throttled(flood_callback, rate=1)
async def berestovitsa_queue_len_passenger(callback: types.CallbackQuery):
    checkpoint_info = Parser("checkpiont", checkpoint="Берестовица", transport="Car")
    await checkpoint_info.len_queue()
    try:
        await callback.message.edit_text(
            text=checkpoint_info.response,
            reply_markup=keyboard.ikb_berestovitsa_passenger(),
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)


@dp.callback_query_handler(text="berestovitsa_an_hour_passenger")
@dp.throttled(flood_callback, rate=1)
async def berestovitsa_an_hour_passenger(callback: types.CallbackQuery):
    checkpoint_info = Parser("stat7", transport="car")
    await checkpoint_info.queue_promotion_per_hour()
    try:
        await callback.message.edit_text(
            text=checkpoint_info.response,
            reply_markup=keyboard.ikb_berestovitsa_passenger(),
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)


@dp.callback_query_handler(text="berestovitsa_an_day_passenger")
@dp.throttled(flood_callback, rate=1)
async def berestovitsa_an_day_passenger(callback: types.CallbackQuery):
    checkpoint_info = Parser("stat7", transport="car")
    await checkpoint_info.queue_promotion_per_day()
    try:
        await callback.message.edit_text(
            text=checkpoint_info.response,
            reply_markup=keyboard.ikb_berestovitsa_passenger(),
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)


@dp.callback_query_handler(text="berestovitsa_cargo")
@dp.throttled(flood_callback, rate=1)
async def berestovitsa_cargo(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=_(
            "Страна: Польша 🇵🇱\nПункт пропуска: Берестовица\nТранспорт: Грузовой  🚛"
        ),
        reply_markup=keyboard.ikb_berestovitsa_cargo(),
    )


@dp.callback_query_handler(text="back_berestovitsa_cargo")
@dp.throttled(flood_callback, rate=1)
async def berestovitsa_back_cargo(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=_("Страна: Польша 🇵🇱\nПункт пропуска: Берестовица"),
        reply_markup=keyboard.ikb_berestovitsa_ts(),
    )


@dp.callback_query_handler(text="berestovitsa_place_in_queue_cargo")
@dp.throttled(flood_callback, rate=1)
async def berestovitsa_place_in_queue_cargo(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    checkpoint_info = Parser("berestovica", user_id=user_id, transport="truck")
    await checkpoint_info.get_place()
    try:
        await callback.message.edit_text(
            text=checkpoint_info.response,
            reply_markup=keyboard.ikb_berestovitsa_cargo(),
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)
    return checkpoint_info._model


@dp.callback_query_handler(text="berestovitsa_queue_len_cargo")
@dp.throttled(flood_callback, rate=1)
async def berestovitsa_queue_len_cargo(callback: types.CallbackQuery):
    checkpoint_info = Parser("checkpoint", checkpoint="Берестовица", transport="Truck")
    await checkpoint_info.len_queue()
    try:
        await callback.message.edit_text(
            text=checkpoint_info.response,
            reply_markup=keyboard.ikb_berestovitsa_cargo(),
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)


@dp.callback_query_handler(text="berestovitsa_an_hour_cargo")
@dp.throttled(flood_callback, rate=1)
async def berestovitsa_an_hour_cargo(callback: types.CallbackQuery):
    checkpoint_info = Parser("stat7", transport="truck")
    await checkpoint_info.queue_promotion_per_hour()
    try:
        await callback.message.edit_text(
            text=checkpoint_info.response,
            reply_markup=keyboard.ikb_berestovitsa_cargo(),
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)


@dp.callback_query_handler(text="berestovitsa_an_day_cargo")
@dp.throttled(flood_callback, rate=1)
async def berestovitsa_an_day_cargo(callback: types.CallbackQuery):
    checkpoint_info = Parser("stat7", transport="truck")
    await checkpoint_info.queue_promotion_per_day()
    try:
        await callback.message.edit_text(
            text=checkpoint_info.response,
            reply_markup=keyboard.ikb_berestovitsa_cargo(),
        )
    except MessageNotModified:
        await bot.answer_callback_query(callback_query_id=callback.id)
