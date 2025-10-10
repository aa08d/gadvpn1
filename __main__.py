import asyncio

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from app.config_loader import load_config
from app.bot.config import BotConfig
from app.bot.middlewares import SessionMiddleware
from app.marzban import init_marzban
from app.bot.handlers import include_routers


async def main() -> None:
    bot_config = load_config(BotConfig, "bot")
    bot = Bot(bot_config.token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    marzban = init_marzban()
    dp = Dispatcher(bot=bot, vpn=marzban)

    dp.update.middleware(SessionMiddleware())

    include_routers(dp)

    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    asyncio.run(main())
