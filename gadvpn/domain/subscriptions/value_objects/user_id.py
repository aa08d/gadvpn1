from uuid import UUID

from gadvpn.domain.common.value_objects import ValueObject


class UserID(ValueObject):
    def __init__(self, user_id: UUID) -> None:
        self._user_id = user_id

    @property
    def value(self) -> UUID:
        return self._user_id
