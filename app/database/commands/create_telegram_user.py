from dataclasses import dataclass

from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models import User, Wallet, TelegramAccount


@dataclass(frozen=True)
class CreateUserCommand:
    telegram_id: int
    username: str
    first_name: str
    last_name: str
    language_code: str


async def create_telegram_user(command: CreateUserCommand, session: AsyncSession) -> User:
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

    await session.commit()
    return user
