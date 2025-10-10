from aiogram.filters import BaseFilter
from aiogram.types import CallbackQuery
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.queries import get_user_by_telegram


class IsAuthorized(BaseFilter):
    async def __call__(self, callback: CallbackQuery, session: AsyncSession) -> bool:
        user = await get_user_by_telegram(callback.from_user.id, session)
        return user is not None
