import asyncio
from tele_bot.settings import conf
from aiogram import Bot, Dispatcher, executor
from tortoise import Tortoise
from tele_bot.utils.cron import start_daemon, close_daemon
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from tele_bot.base.monitoring import start_monitoring


storage = RedisStorage2("localhost", 6379, db=5)
bot = Bot(token=conf.token)
dp = Dispatcher(bot=bot, storage=storage)
scheduler = AsyncIOScheduler(timezone="Europe/Minsk")
scheduler.add_job(start_monitoring, trigger="interval", seconds=5, kwargs={"bot": bot})
scheduler.start()


async def setup_middleware():
    from tele_bot.middleware import (
        AllUsersMiddleware,
        ServiceMiddlewere,
        i18n,
        RegisterUserMiddleware,
    )

    dp.setup_middleware(RegisterUserMiddleware())
    dp.setup_middleware(AllUsersMiddleware())
    dp.setup_middleware(ServiceMiddlewere())
    dp.setup_middleware(i18n)


async def on_startapp(executor):
    from tele_bot import handlers
    from tele_bot import admin

    await setup_middleware()
    await Tortoise.init(config=conf.DB_CONFIG)
    await Tortoise.generate_schemas()


async def on_shotdown(executor):
    await Tortoise.close_connections()
    await dp.storage.close()
    await dp.storage.wait_closed()


def start_bot():
    try:
        start_daemon()
        loop = asyncio.get_event_loop()
        executor.start_polling(
            dp,
            loop=loop,
            on_startup=on_startapp,
            on_shutdown=on_shotdown,
            skip_updates=True,
        )
    finally:
        close_daemon()
