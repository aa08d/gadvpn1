from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models import User, TelegramAccount


async def get_user_by_telegram(telegram_id: int, session: AsyncSession) -> User | None:
    stmt = select(TelegramAccount.user_id).filter(TelegramAccount.id == telegram_id)
    result = await session.execute(stmt)
    user_id = result.scalars().first()

    if not user_id:
        return

    stmt = select(User).filter(User.id == user_id)
    result = await session.execute(stmt)
    user = result.scalars().first()
    return user
