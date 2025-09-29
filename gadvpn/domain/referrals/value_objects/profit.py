from decimal import Decimal

from gadvpn.domain.common.value_objects import ValueObject


class Profit(ValueObject):
    def __init__(self, profit: Decimal) -> None:
        self._profit = profit

    @classmethod
    def create(cls) -> "Profit":
        return cls(Decimal(0))

    def add(self, profit: "Profit") -> "Profit":
        return Profit(self._profit + profit._profit)

    @property
    def value(self) -> Decimal:
        return self._profit
