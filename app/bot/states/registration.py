from aiogram.fsm.state import State, StatesGroup


class UserRegistration(StatesGroup):
    language = State()
