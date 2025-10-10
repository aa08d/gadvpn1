from datetime import datetime, UTC

from aiogram import Router, F
from aiogram.types import CallbackQuery

from app.bot.filters.callback_data import MenuCallback, PaymentCallback
from app.bot.keyboards import payment_days_keyboard, get_invoice_keyboard
from app.payment import create_payment
from app.bot.messages import payment_message, invoice_message


router = Router()


@router.callback_query(MenuCallback.filter(F.category == "payment"))
async def payment_category_callback(callback: CallbackQuery) -> None:
    await callback.message.edit_text(
        text=payment_message,
        reply_markup=payment_days_keyboard,
    )


prices = {
    "30": 100,
    "90": 270,
    "180": 510,
    "360": 960,
}


@router.callback_query(PaymentCallback.filter())
async def invoice_callback(
    callback: CallbackQuery,
    callback_data: PaymentCallback,
) -> None:
    amount = prices[str(callback_data.days)]
    payment_url, payment_id = create_payment(amount=amount, days=int(callback_data.days))
    await callback.message.answer(
        text=invoice_message.format(
            days=callback_data.days,
            date=datetime.now(UTC).date(),
        ),
        reply_markup=get_invoice_keyboard(url=payment_url),
    )
