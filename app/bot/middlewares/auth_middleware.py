from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware, Bot
from aiogram.types import TelegramObject, Message, CallbackQuery, PreCheckoutQuery
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.queries import get_user_by_telegram
from app.bot.messages import choice_language_message
from app.bot.keyboards import choice_language_keyboard


class AuthMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        print("start")
        # if event.callback_query and event.callback_query.data.startswith("language"):
        #     return await handler(event, data)

        bot: Bot = data.get("bot")
        session: AsyncSession = data.get("session")
        user_id = data["event_from_user"].id
        user = await get_user_by_telegram(user_id, session)

        print(user)

        if user is None:
            await bot.send_message(
                chat_id=user_id,
                text=choice_language_message,
                reply_markup=choice_language_keyboard,
            )
            return

        return await handler(event, data)
