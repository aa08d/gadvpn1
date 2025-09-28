from uuid import UUID

from uuid6 import uuid7

from gadvpn.domain.common.value_objects import ValueObject


class ReferralID(ValueObject):
    def __init__(self, referral_id: UUID) -> None:
        self._referral_id = referral_id

    @classmethod
    def create(cls) -> "ReferralID":
        return cls(uuid7())

    @property
    def value(self) -> UUID:
        return self._referral_id
