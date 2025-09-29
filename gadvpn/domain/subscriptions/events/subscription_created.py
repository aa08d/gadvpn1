from dataclasses import dataclass
from uuid import UUID

from gadvpn.domain.common.events import Event


@dataclass(frozen=True)
class SubscriptionCreated(Event):
    subscription_id: UUID
    expire_date: int
    user_id: UUID
