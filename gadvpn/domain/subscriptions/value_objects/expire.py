from datetime import datetime, UTC, timedelta

from gadvpn.domain.common.value_objects import ValueObject


TRIAL_PERIOD_DAYS = 10


class ExpireDays(ValueObject):
    def __init__(self, days: int):
        self._days = days

    @property
    def value(self) -> int:
        return self._days


class ExpireDate(ValueObject):
    def __init__(self, unix_timestamp: int) -> None:
        self._expire_date = unix_timestamp

    @classmethod
    def create(cls) -> "ExpireDate":
        expire_at = datetime.now(UTC) + timedelta(days=TRIAL_PERIOD_DAYS)
        return cls(int(expire_at.timestamp()))

    def extend(self, days: ExpireDays) -> "ExpireDate":
        if not self.is_expired():
            expire_date = datetime.fromtimestamp(self._expire_date) + timedelta(days=days.value)
        else:
            expire_date = datetime.now(UTC) + timedelta(days=days.value)

        return ExpireDate(int(expire_date.timestamp()))

    def is_expired(self) -> bool:
        return datetime.now(UTC).timestamp() > self._expire_date

    @property
    def value(self) -> int:
        return self._expire_date
