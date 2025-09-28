from decimal import Decimal

from gadvpn.domain.common.value_objects import ValueObject


class Profit(ValueObject):
    def __init__(self, profit: Decimal = Decimal(0)) -> None:
        self._profit = profit

    def add(self, amount: Decimal) -> None:
        self._profit = self._profit + amount

    @property
    def value(self) -> Decimal:
        return self._profit
