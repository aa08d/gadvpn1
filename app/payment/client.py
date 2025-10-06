import yookassa

from uuid6 import uuid7

from app.config_loader import load_config

from .config import PaymentConfig


config = load_config(PaymentConfig, 'payment')


yookassa.Configuration.account_id = config.account_id
yookassa.Configuration.secret_key = config.secret_key


def create(amount: int, days: int) -> yookassa.Payment:
    payment_id = str(uuid7())
    payment = yookassa.Payment.create(
        {
            "amount": {
                "value": amount,
                "currency": "RUB",
            },
            "payment_method_data": {
                "type": "sbp",
            },
            "confirmation": {
                "type": "redirect",
                "return_url": "https://t.me/GadVPNBot"
            },
            "capture": True,
            "metadata": {
                "days": days
            },
            "description": "Оплата товаров и услуг"
        },
        payment_id,
    )

    return payment.confirmation.confirmation_url, payment.id
