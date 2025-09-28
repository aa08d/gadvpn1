from uuid import UUID
from dataclasses import dataclass

from gadvpn.domain.common.events import Event


@dataclass(frozen=True)
class FullNameUpdated(Event):
    user_id: UUID
    first_name: str
    last_name: str
