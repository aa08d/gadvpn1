from aiogram.filters.callback_data import CallbackData


class PaymentCallback(CallbackData, prefix="payment"):
    days: int
