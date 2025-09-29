from uuid import UUID

from uuid6 import uuid7

from gadvpn.domain.common.value_objects import ValueObject


class SubscriptionID(ValueObject):
    def __init__(self, subscription_id: UUID) -> None:
        self._subscription_id = subscription_id

    @classmethod
    def create(cls) -> "SubscriptionID":
        return cls(uuid7())

    @property
    def value(self) -> UUID:
        return self._subscription_id
