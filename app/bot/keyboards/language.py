from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.bot.filters.callback_data import LanguageCallback


language_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🇷🇺 ru",
                callback_data=LanguageCallback(language="ru").pack(),
            ),
            InlineKeyboardButton(
                text="🇬🇧 en",
                callback_data=LanguageCallback(language="en").pack(),
            ),
        ],
    ],
)
