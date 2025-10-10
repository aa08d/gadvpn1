from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.filters import CommandStart, CommandObject
from aiogram.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession

from app.bot.filters import IsAuthorized
from app.bot.filters.callback_data import LanguageCallback
from app.bot.keyboards import menu_keyboard, language_keyboard
from app.bot.messages import welcome_message
from app.bot.states import UserRegistration
from app.database.queries import get_user_by_telegram
from app.database.commands import (
    create_telegram_user,
    CreateUserCommand,
    create_telegram_referral,
    CreateTelegramReferralCommand,
)
from app.marzban import VPNClient


router = Router()


@router.message(CommandStart(deep_link=True, deep_link_encoded=True, magic=F.args), ~IsAuthorized())
async def start_cmd_from_referral(
    message: Message,
    command: CommandObject,
    state: FSMContext,
    session: AsyncSession,
) -> None:
    from_user = await get_user_by_telegram(int(command.args), session)

    if from_user is not None:
        await state.update_data(from_user=from_user.id)

    await state.set_state(UserRegistration.language)
    await message.answer(
        "🌐 Please choose your language:",
        reply_markup=language_keyboard,
    )


@router.callback_query(UserRegistration.language, LanguageCallback.filter(), ~IsAuthorized())
async def register_referral_callback(
    callback: CallbackQuery,
    callback_data: LanguageCallback,
    state: FSMContext,
    session: AsyncSession,
    vpn: VPNClient,
) -> None:
    state_data = await state.get_data()
    from_user_id = state_data.get("from_user")
    command = CreateTelegramReferralCommand(
        telegram_id=callback.from_user.id,
        username=callback.from_user.username,
        first_name=callback.from_user.first_name,
        last_name=callback.from_user.last_name,
        language_code=callback_data.language,
        from_user=from_user_id,
    )
    user = await create_telegram_referral(command, session)
    await vpn.create_user(user_id=user.id)
    await vpn.extend_subscription(from_user_id, 10)
    await callback.message.edit_text(
        text=welcome_message.format(name=user.first_name),
        reply_markup=menu_keyboard,
    )
    await callback.answer()
    await state.clear()


@router.callback_query(LanguageCallback.filter(), ~IsAuthorized())
async def register_user_callback(
    callback: CallbackQuery,
    callback_data: LanguageCallback,
    session: AsyncSession,
    vpn: VPNClient,
) -> None:
    command = CreateUserCommand(
        telegram_id=callback.from_user.id,
        username=callback.from_user.username,
        first_name=callback.from_user.first_name,
        last_name=callback.from_user.last_name,
        language_code=callback_data.language,
    )
    user = await create_telegram_user(command, session)
    await vpn.create_user(user_id=user.id)
    await callback.message.edit_text(
        text=welcome_message.format(name=user.first_name),
        reply_markup=menu_keyboard,
    )
    await callback.answer()


@router.message(CommandStart(), IsAuthorized())
async def start_cmd(message: Message) -> None:
    await message.answer(
        text=welcome_message.format(name=message.from_user.first_name),
        reply_markup=menu_keyboard,
    )


@router.callback_query(~IsAuthorized())
async def unregistered_user_callback(callback: CallbackQuery) -> None:
    await callback.message.answer(
        "🌐 Please choose your language:",
        reply_markup=language_keyboard,
    )
    await callback.answer()


@router.message(~IsAuthorized())
async def unregistered_user_message(message: Message) -> None:
    await message.answer(
        "🌐 Please choose your language:",
        reply_markup=language_keyboard,
    )
