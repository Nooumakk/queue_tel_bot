import redis.asyncio as redis
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Message, callback_query
from tele_bot.db.models import User
from tortoise.exceptions import IntegrityError, DoesNotExist
from aiogram.dispatcher.handler import CancelHandler
from tele_bot.db.models import User
from datetime import datetime
from aiogram.contrib.middlewares.i18n import I18nMiddleware
from tele_bot.settings import conf
from aiogram import types
from tortoise.exceptions import DoesNotExist


class LanguageMiddlewere(I18nMiddleware):
    async def get_user_locale(self, action: str, args):
        self.default = "ru"
        user = types.User.get_current()
        try:
            r = await redis.from_url("redis://localhost")
            async with r.pipeline(transaction=True) as pipe:
                language = await r.get(user.id)
                if language:
                    return language.decode("utf-8")
                language = await User.get(telegram_id=user.id).values("language_code")
                await pipe.set(
                    user.id, language["language_code"].encode("utf-8"), 300
                ).execute()
        except DoesNotExist:
            return self.default
        return language["language_code"]


class RegisterUserMiddleware(BaseMiddleware):
    async def on_pre_process_callback_query(
        self, callback: callback_query, data_from_user
    ):
        if callback["data"] in ("ru", "en", "pl"):
            user_code = (
                "ru"
                if callback["data"] == "ru"
                else ("en" if callback["data"] == "en" else "pl")
            )
            try:
                user = await User.get(telegram_id=callback.from_user.id)
                await user.update_from_dict({"language_code": user_code})
                await user.save()
                r = await redis.from_url("redis://localhost")
                async with r.pipeline(transaction=True) as pipe:
                    await pipe.set(
                        callback.from_user.id, user_code.encode("utf-8"), 300
                    ).execute()
            except DoesNotExist:
                try:
                    await User.create(
                        telegram_id=callback.from_user.id,
                        username=callback.from_user.username,
                        first_name=callback.from_user.first_name,
                        language_code=user_code,
                    )
                except IntegrityError:
                    ...


class AllUsersMiddleware(BaseMiddleware):
    async def on_post_process_callback_query(
        self, callback: callback_query, numbers, data
    ):
        if callback["data"] in ("del_bus", "del_passenger", "del_cargo"):
            for number in numbers[0]:
                if number[0] != "id":
                    if number[1] != None:
                        return
            await numbers[0].delete()


class ServiceMiddlewere(BaseMiddleware):
    async def on_pre_process_message(self, message: Message, data: dict):
        if message["text"] == "/admin":
            user = await User.get(telegram_id=message.from_user.id)
            if not user.is_staff:
                if user.telegram_id != conf.admin_id:
                    raise CancelHandler()
                user.is_staff = True
                await user.save()

    async def on_post_process_callback_query(
        self, callback: callback_query, user: User, data
    ):
        if user:
            if user[0].__class__.__name__ == "User":
                await user[0].update_from_dict({"last_active": datetime.now()})
                await user[0].save()


i18n = LanguageMiddlewere(conf.I18N_DOMAIN, conf.LOCALES_DIRS)
_ = i18n.gettext
