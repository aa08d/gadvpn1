from gadvpn.domain.common.entities import AggregateRoot
from gadvpn.domain.referrals.value_objects import ReferralID, Profit, FromUser, ReferredAt
from gadvpn.domain.referrals.events import ReferralCreated, ProfitUpdated

from uuid6 import uuid7
from decimal import Decimal


class Referral(AggregateRoot):
    def __init__(
        self,
        referral_id: ReferralID,
        profit: Profit,
        from_user: FromUser,
        referred_at: ReferredAt,
    ) -> None:
        super().__init__()
        self.referral_id = referral_id
        self.profit = profit
        self.from_user = from_user
        self.referred_at = referred_at

    @classmethod
    def create(cls, from_user: FromUser) -> "Referral":
        referral = cls(
            referral_id=ReferralID.create(),
            profit=Profit.create(),
            from_user=from_user,
            referred_at=ReferredAt.create(),
        )
        referral._record_event(
            ReferralCreated(
                referral_id=referral.referral_id.value,
                profit=referral.profit.value,
                from_user=referral.from_user.value,
                referred_at=referral.from_user.value,
            )
        )
        return referral

    def add_profit(self, profit: Profit) -> None:
        self.profit.add(profit)
        self._record_event(
            ProfitUpdated(
                referral_id=self.referral_id.value,
                profit=profit.value,
                total=self.profit.value,
            )
        )
