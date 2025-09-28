from datetime import datetime, UTC

from gadvpn.domain.common.value_objects import ValueObject


class ReferredAt(ValueObject):
    def __init__(self, referred_at: int) -> None:
        self._referred_at = referred_at

    @classmethod
    def create(cls) -> "ReferredAt":
        return cls(datetime.now(UTC).timestamp())

    @property
    def value(self) -> int:
        return self._referred_at
