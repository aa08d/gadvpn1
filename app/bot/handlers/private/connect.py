from aiogram import Router, F
from aiogram.types import CallbackQuery
from sqlalchemy.ext.asyncio import AsyncSession

from app.bot.filters.callback_data import MenuCallback, ChoiceOSCallback
from app.bot.keyboards import os_keyboard, get_connect_keyboard
from app.marzban import VPNClient
from app.database.queries import get_user_by_telegram
from app.bot.messages import manual_message, connect_category_message


router = Router()


@router.callback_query(MenuCallback.filter(F.category == "connect"))
async def connect_callback(callback: CallbackQuery) -> None:
    await callback.message.edit_text(
        text=connect_category_message,
        reply_markup=os_keyboard,
    )


download_links = {
    "android": "https://play.google.com/store/apps/details?id=com.v2raytun.android",
    "ios": "https://apps.apple.com/en/app/v2raytun/id6476628951",
    "windows": "https://storage.v2raytun.com/v2RayTun_Setup.exe",
    "mac_os": "https://apps.apple.com/en/app/v2raytun/id6476628951",
}
deeplink_template = "https://gadvpn-preview.ru/?target={subscription_url}"


@router.callback_query(ChoiceOSCallback.filter())
async def os_chose_callback(
    callback: CallbackQuery,
    callback_data: ChoiceOSCallback,
    vpn: VPNClient,
    session: AsyncSession,
) -> None:
    user = await get_user_by_telegram(callback.from_user.id, session)
    vpn_user = await vpn.get_user(user.id)
    download_link = download_links[callback_data.os]
    deeplink = deeplink_template.format(vpn_user.subscription_url)

    await callback.message.edit_text(
        text=manual_message,
        reply_markup=get_connect_keyboard(download_link, deeplink)
    )
