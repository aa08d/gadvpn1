from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.bot.filters import ChoiceLanguageCallbackData


choice_language_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🇷🇺 ru",
                callback_data=ChoiceLanguageCallbackData(language="ru").pack(),
            ),
            InlineKeyboardButton(
                text="🇬🇧 en",
                callback_data=ChoiceLanguageCallbackData(language="en").pack(),
            )
        ]
    ]
)
