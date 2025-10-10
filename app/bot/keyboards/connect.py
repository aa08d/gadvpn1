from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.bot.filters.callback_data import ChoiceOSCallback


os_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🤖 Android",
                callback_data=ChoiceOSCallback(os="android").pack(),
            ),
            InlineKeyboardButton(
                text="🍎 iOS",
                callback_data=ChoiceOSCallback(os="ios").pack(),
            ),
        ],
        [
            InlineKeyboardButton(
                text="🖥️  Windows",
                callback_data=ChoiceOSCallback(os="windows").pack(),
            ),
            InlineKeyboardButton(
                text="💻 MacOS",
                callback_data=ChoiceOSCallback(os="mac_os").pack(),
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
