from aiogram import Dispatcher

from .register_user import router as register_user_router


def include_private_routers(dp: Dispatcher) -> None:
    dp.include_router(register_user_router)
