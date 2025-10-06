from dataclasses import dataclass


@dataclass
class PaymentConfig:
    account_id: str
    secret_key: str
