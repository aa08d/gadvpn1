from aiogram.filters.callback_data import CallbackData


class ChoiceOSCallbackData(CallbackData, prefix="os"):
    os: str
