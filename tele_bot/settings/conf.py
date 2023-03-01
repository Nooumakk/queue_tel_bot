import os
from pathlib import Path
from dotenv import load_dotenv


__all__ = (
    "BASE_DIR",
    "user_agent",
    "token",
    "DB_CONFIG",
    "LOCALES_DIRS",
    "I18N_DOMAIN",
    "admin_id",
)


BASE_DIR = Path(__file__).parent.parent.absolute()
dorenv_path = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(dorenv_path):
    load_dotenv(dorenv_path)


LOCALES_DIRS = BASE_DIR / "locales"
I18N_DOMAIN = "mybot"


user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
token = os.getenv("TOKEN")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
admin_id = os.getenv("ADMIN_ID")


DB_CONFIG = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.asyncpg",
            "credentials": {
                "host": "localhost",
                "port": "5432",
                "user": db_user,
                "password": db_password,
                "database": "tele_bot",
            },
        },
    },
    "apps": {
        "models": {
            "models": ["tele_bot.db.models"],
            "default_connection": "default",
        }
    },
}
