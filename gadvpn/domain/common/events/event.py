from abc import ABC
from uuid import UUID
from datetime import datetime, UTC

from dataclasses import dataclass, field

from uuid6 import uuid7


@dataclass(frozen=True)
class Event(ABC):
    event_id: UUID = field(init=False, kw_only=True, default_factory=uuid7)
    event_timestamp: datetime = field(init=False, kw_only=True, default=datetime.now(UTC))
