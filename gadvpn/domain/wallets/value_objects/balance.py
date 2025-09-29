from decimal import Decimal

from gadvpn.domain.common.value_objects import ValueObject


DEFAULT_BALANCE = Decimal('0.00')


class Balance(ValueObject):
    def __init__(self, balance: Decimal) -> None:
        self._balance = balance

    @classmethod
    def create(cls) -> "Balance":
        return cls(DEFAULT_BALANCE)

    @property
    def balance(self) -> Decimal:
        return self._balance
