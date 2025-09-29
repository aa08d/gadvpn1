from enum import Enum

from gadvpn.domain.common.value_objects import ValueObject


class CurrencyEnum(str, Enum):
    RUB = 'RUB'
    USD = 'USD'


class Currency(ValueObject):
    def __init__(self, currency: CurrencyEnum) -> None:
        self._currency = currency

    @property
    def value(self) -> CurrencyEnum:
        return self._currency
