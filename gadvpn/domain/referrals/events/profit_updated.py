from uuid import UUID
from dataclasses import dataclass
from decimal import Decimal

from gadvpn.domain.common.events import Event


@dataclass(frozen=True)
class ProfitUpdated(Event):
    referral_id: UUID
    profit: Decimal
    total: Decimal
