from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.bot.filters import ChoiceOSCallbackData


os_choice_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🤖 Android",
                callback_data=ChoiceOSCallbackData(os="android").pack(),
            ),
            InlineKeyboardButton(
                text="🍎 iOS",
                callback_data=ChoiceOSCallbackData(os="ios").pack(),
            ),
        ],
        [
            InlineKeyboardButton(
                text="🖥️  Windows",
                callback_data=ChoiceOSCallbackData(os="windows").pack(),
            ),
            InlineKeyboardButton(
                text="💻 MacOS",
                callback_data=ChoiceOSCallbackData(os="mac_os").pack(),
            ),
        ],
    ],
)


def get_connect_keyboard(download_link: str, deeplink: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="📥 Скачать приложение", url=download_link),
            ],
            [
                InlineKeyboardButton(text="🔑 Добавить ключ", url=deeplink)
            ],
        ],
    )
