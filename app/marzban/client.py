from datetime import datetime, timedelta, timezone
from uuid import UUID

from marzban_api_client import Client, AuthenticatedClient
from marzban_api_client.models.body_admin_token_api_admin_token_post import BodyAdminTokenApiAdminTokenPost
from marzban_api_client.api.admin import admin_token
from marzban_api_client.api.user import add_user, modify_user, get_user, get_users
from marzban_api_client.models import (
    UserCreate,
    UserModify,
    UserCreateProxies,
    UserResponse,
)

from .config import MarzbanConfig


proxies = UserCreateProxies.from_dict(
    {
        "vless": {
            "flow": "xtls-rprx-vision",
        },
    }
)


class VPNClient:
    def __init__(self, config: MarzbanConfig) -> None:
        self._config = config

    async def create_user(self, user_id: UUID, username:  str | None, telegram_id: int) -> None:
        expire = datetime.timestamp(
            datetime.now(timezone(timedelta(hours=3))) + timedelta(days=10)
        )
        user = UserCreate(
            username=str(user_id),
            proxies=proxies,
            expire=int(expire),
            note=f"Username: {username}; Telegram ID: {telegram_id}"
        )
        await add_user.asyncio(client=self.client, body=user)

    async def extend_subscription(self, user_id: UUID, days: int) -> None:
        user = await self.get_user(user_id)

        if datetime.timestamp(datetime.utcnow()) > user.expire:
            expire_date = datetime.timestamp(
                datetime.fromtimestamp(datetime.utcnow()) + timedelta(days=days)
            )
        else:
            expire_date = datetime.timestamp(
                datetime.fromtimestamp(user.expire) + timedelta(days=days)
            )

        payload = UserModify(expire=int(expire_date))
        await modify_user.asyncio(user_id, client=self.client, body=payload)

    async def get_user(self, user_id: UUID) -> UserResponse:
        user = await get_user.asyncio(str(user_id), client=self.client)
        return user

    async def get_users(self) -> list[UserResponse]:
        users = await get_users.asyncio(client=self.client)
        return users.users

    @property
    async def client(self) -> None:
        async with Client(base_url=self._config.url) as client:
            login_data = BodyAdminTokenApiAdminTokenPost(
                username=self._config.username,
                password=self._config.password,
            )
            token_response = await admin_token.asyncio(client=client, body=login_data)
            return AuthenticatedClient(base_url=self._config.url, token=token_response.access_token)
