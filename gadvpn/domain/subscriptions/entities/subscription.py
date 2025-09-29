from gadvpn.domain.common.entities import AggregateRoot
from gadvpn.domain.subscriptions.value_objects import (
    SubscriptionID,
    ExpireDate,
    ExpireDays,
    UserID,
)
from gadvpn.domain.subscriptions.events import SubscriptionCreated, SubscriptionExtended


class Subscription(AggregateRoot):
    def __init__(
        self,
        subscription_id: SubscriptionID,
        expire_date: ExpireDate,
        user_id: UserID,
    ) -> None:
        super().__init__()
        self.subscription_id = subscription_id
        self.expire_date = expire_date
        self.user_id = user_id

    @classmethod
    def create(cls, user_id: UserID) -> "Subscription":
        subscription = cls(
            subscription_id=SubscriptionID.create(),
            expire_date=ExpireDate.create(),
            user_id=user_id,
        )
        subscription._record_event(
            SubscriptionCreated(
                subscription_id=subscription.subscription_id.value,
                expire_date=subscription.expire_date.value,
                user_id=subscription.user_id.value,
            )
        )
        return subscription

    def extend(self, days: ExpireDays) -> None:
        self.expire_date = self.expire_date.extend(days)
        self._record_event(
            SubscriptionExtended(
                subscription_id=self.subscription_id.value,
                expire_date=self.expire_date.value,
                user_id=self.user_id.value,
            )
        )
