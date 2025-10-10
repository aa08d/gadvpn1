from aiogram.filters.callback_data import CallbackData


class ChoiceOSCallback(CallbackData, prefix="os"):
    os: str
