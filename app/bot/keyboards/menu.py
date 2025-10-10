from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.bot.filters.callback_data import MenuCallback


menu_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="⚡ Подключиться",
                callback_data=MenuCallback(category="connect").pack(),
            ),
            InlineKeyboardButton(
                text="💳 Пополнить",
                callback_data=MenuCallback(category="payment").pack(),
            ),
        ],
        [
            InlineKeyboardButton(
                text="👥 Пригласить друзей",
                callback_data=MenuCallback(category="referrals").pack(),
            ),
        ],
        [
            InlineKeyboardButton(text="🛠 Поддержка", url="t.me/GadVpnSupport"),
        ],
    ],
)
