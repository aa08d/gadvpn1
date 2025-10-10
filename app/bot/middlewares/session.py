from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from app.database.base import build_sa_engine, build_sa_session_factory


class SessionMiddleware(BaseMiddleware):
    def __init__(self):
        self.engine = build_sa_engine()
        self.session_factory = build_sa_session_factory(self.engine)

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        async with self.session_factory() as session:
            data["session"] = session
            return await handler(event, data)
