from typing import Literal

from aiogram.filters.callback_data import CallbackData


class ChoiceLanguageCallbackData(CallbackData, prefix="language"):
    language: Literal["ru", "en"]
