from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.bot.filters.menu import MenuCallbackData


main_menu_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="⚡ Подключиться",
            callback_data=MenuCallbackData(category="connect").pack(),
        ),
        InlineKeyboardButton(
            text="💳 Пополнить",
            callback_data=MenuCallbackData(category="payment").pack(),
        ),
    ],
    [
        InlineKeyboardButton(
            text="👥 Пригласить друзей",
            callback_data=MenuCallbackData(category="invite_friends").pack(),
        ),
    ],
    [
        InlineKeyboardButton(text="🛠 Поддержка", url="t.me/GadVpnSupport"),
    ],
])
