from gadvpn.domain.common.entities import Entity
from gadvpn.domain.user.value_objects import UserID, FullName


class User(Entity):
    def __init__(self, user_id: UserID, full_name: FullName) -> None:
        self.user_id = user_id
        self.full_name = full_name

    @classmethod
    def create(cls, full_name: FullName) -> "User":
        user_id = UserID.create()
        user = cls(user_id, full_name)
        return user

    def set_full_name(self, full_name: FullName) -> None:
        self.full_name = full_name
