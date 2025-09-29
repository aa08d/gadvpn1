from uuid import UUID

from uuid6 import uuid7

from gadvpn.domain.common.value_objects import ValueObject


class WalletID(ValueObject):
    def __init__(self, wallet_id: UUID) -> None:
        self._wallet_id = wallet_id

    @classmethod
    def create(cls) -> "WalletID":
        return cls(uuid7())

    @property
    def value(self) -> UUID:
        return self._wallet_id
