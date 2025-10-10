from aiogram import Router, F
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, CopyTextButton
from aiogram.utils.deep_linking import create_start_link

from app.bot.filters.callback_data import MenuCallback


router = Router()


@router.callback_query(MenuCallback.filter(F.category == "referrals"))
async def referral_category_callback(callback: CallbackQuery) -> None:
    referral_link = await create_start_link(
        bot=callback.bot,
        payload=str(callback.from_user.id),
        encode=True,
    )
    await callback.message.edit_text(
        text="Ваша реферальная ссылка",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="Скопировать",
                        copy_text=CopyTextButton(text=referral_link),
                    )
                ]
            ]
        )
    )
    await callback.answer()
