from .client import VPNClient
from .config import MarzbanConfig

from app.config_loader import load_config


def init_marzban() -> VPNClient:
    config = load_config(MarzbanConfig, "marzban")
    client = VPNClient(config)
    return client
