from aiogram import Dispatcher

from .start import router as register_user_router
from .connect import router as connect_router
from .referral import router as referral_router
from .payment import router as payment_router


def include_private_routers(dp: Dispatcher) -> None:
    dp.include_router(register_user_router)
    dp.include_router(connect_router)
    dp.include_router(referral_router)
    dp.include_router(payment_router)
