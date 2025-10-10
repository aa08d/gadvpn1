from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.bot.filters.callback_data import PaymentCallback, MenuCallback


payment_days_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
                [
                    InlineKeyboardButton(
                      text="30 дней",
                      callback_data=PaymentCallback(days="30").pack(),
                    ),
                    InlineKeyboardButton(
                      text="90 дней",
                      callback_data=PaymentCallback(days="90").pack(),
                    ),
                ],
                [
                    InlineKeyboardButton(
                        text="180 дней",
                        callback_data=PaymentCallback(days="180").pack(),
                    ),
                    InlineKeyboardButton(
                        text="360 дней",
                        callback_data=PaymentCallback(days="360").pack(),
                    ),
                ],
                [
                    InlineKeyboardButton(
                        text="⬅️ Назад",
                        callback_data=MenuCallback(category="main").pack(),
                    ),
                ],
            ],
)


def get_invoice_keyboard(url: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=f"💳 Оплатить", url=url),
            ],
        ],
    )
