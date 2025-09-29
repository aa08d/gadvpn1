from dataclasses import dataclass
from uuid import UUID

from gadvpn.domain.common.events import Event
from gadvpn.domain.wallets.value_objects import CurrencyEnum


@dataclass(frozen=True)
class CurrencyUpdated(Event):
    wallet_id: UUID
    currency: CurrencyEnum
