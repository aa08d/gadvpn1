from uuid import UUID
from decimal import Decimal
from dataclasses import dataclass

from gadvpn.domain.common.events import Event


@dataclass(frozen=True)
class ReferralCreated(Event):
    referral_id: UUID
    profit: Decimal
    from_user: UUID
    referred_at: int
