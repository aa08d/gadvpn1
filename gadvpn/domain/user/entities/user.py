from gadvpn.domain.common.entities import Entity, AggregateRoot
from gadvpn.domain.user.value_objects import UserID, FullName
from gadvpn.domain.user.events import UserCreated, FullNameUpdated


class User(Entity, AggregateRoot):
    def __init__(self, user_id: UserID, full_name: FullName) -> None:
        super().__init__()
        self.user_id = user_id
        self.full_name = full_name

    @classmethod
    def create(cls, full_name: FullName) -> "User":
        user = cls(UserID.create(), full_name)
        user._record_event(
            UserCreated(
                user_id=user.user_id.value,
                first_name=user.full_name.first_name,
                last_name=user.full_name.last_name,
            )
        )
        return user

    def set_full_name(self, full_name: FullName) -> None:
        self.full_name = full_name
        self._record_event(
            FullNameUpdated(
                user_id=self.user_id.value,
                first_name=self.full_name.first_name,
                last_name=self.full_name.last_name,
            )
        )
