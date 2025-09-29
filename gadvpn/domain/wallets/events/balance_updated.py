from dataclasses import dataclass
from decimal import Decimal
from uuid import UUID

from gadvpn.domain.common.events import Event


@dataclass(frozen=True)
class BalanceUpdated(Event):
    wallet_id: UUID
    balance: Decimal
