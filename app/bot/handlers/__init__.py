from aiogram import Dispatcher

from .private import include_private_routers


def include_routers(dp: Dispatcher) -> None:
    include_private_routers(dp)
