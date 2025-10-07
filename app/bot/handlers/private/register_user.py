from aiogram import Router
from aiogram.types import CallbackQuery
from sqlalchemy.ext.asyncio import AsyncSession

from app.bot.filters import ChoiceLanguageCallbackData
from app.database.commands import create_telegram_user, CreateUserCommand
from app.bot.messages import welcome_message
from app.bot.keyboards import main_menu_keyboard
from app.marzban import VPNClient


router = Router()


@router.callback_query(ChoiceLanguageCallbackData.filter())
async def register_user(
    callback: CallbackQuery,
    callback_data: ChoiceLanguageCallbackData,
    session: AsyncSession,
    marzban: VPNClient,
) -> None:
    command = CreateUserCommand(
        telegram_id=callback.from_user.id,
        username=callback.from_user.username,
        first_name=callback.from_user.first_name,
        last_name=callback.from_user.last_name,
        language_code=callback_data.language,
    )
    user = await create_telegram_user(command, session)
    await callback.message.edit_text(
        text=welcome_message.format(name=user.first_name),
        reply_markup=main_menu_keyboard,
    )
    await marzban.create_user(user_id=user.id)
