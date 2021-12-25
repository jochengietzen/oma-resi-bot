"""
Configuration module
"""
import os

from oma_resi_bot.models.base_pydantic import YamlBaseModel


# pylint: disable=too-few-public-methods
class Config(YamlBaseModel):
    """
    Basic config model
    """

    admin_user: str
    bot_token: str


TOKEN = os.getenv("TELEGRAM_BOT", "UNSET")

config_path = os.getenv(
    "CONFIG_PATH",
    os.path.join(os.path.dirname(__file__), "..", "..", "..", "dev", "config.yaml"),
)

config = Config.from_yaml(config_path)
config.bot_token = TOKEN
