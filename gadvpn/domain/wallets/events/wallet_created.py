from dataclasses import dataclass
from decimal import Decimal
from uuid import UUID

from gadvpn.domain.common.events import Event
from gadvpn.domain.wallets.value_objects import CurrencyEnum


@dataclass(frozen=True)
class WalletCreated(Event):
    wallet_id: UUID
    balance: Decimal
    currency: CurrencyEnum
    user_id: UUID
