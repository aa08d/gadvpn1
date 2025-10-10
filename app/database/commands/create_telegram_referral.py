from dataclasses import dataclass
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models import User, Wallet, TelegramAccount, Referral


@dataclass(frozen=True)
class CreateTelegramReferralCommand:
    telegram_id: int
    username: str
    first_name: str
    last_name: str
    language_code: str
    from_user: UUID


async def create_telegram_referral(command: CreateTelegramReferralCommand, session: AsyncSession) -> User:
    user = User(
        first_name=command.first_name,
        last_name=command.last_name,
        language_code=command.language_code,
    )
    session.add(user)
    await session.flush()

    wallet = Wallet(user_id=user.id)
    session.add(wallet)

    telegram = TelegramAccount(
        id=command.telegram_id,
        username=command.username,
        user_id=user.id,
    )
    session.add(telegram)

    referral = Referral(
        from_user_id=command.from_user,
        user_id=user.id,
    )
    session.add(referral)

    await session.commit()
    return user
