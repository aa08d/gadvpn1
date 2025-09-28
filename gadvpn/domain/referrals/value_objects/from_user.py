from uuid import UUID

from gadvpn.domain.common.value_objects import ValueObject


class FromUser(ValueObject):
    def __init__(self, from_user: UUID) -> UUID:
        self._from_user = from_user

    @property
    def value(self) -> UUID:
        return self._from_user
