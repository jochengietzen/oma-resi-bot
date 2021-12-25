"""
The basic bot functionality for startup, shutdown and dispatcher/updater handling
"""
# pylint: disable=global-variable-not-assigned,invalid-name
from typing import Tuple

from telegram.ext import Dispatcher, Updater

from oma_resi_bot.models.config import config
from oma_resi_bot.utils.logger import logger
from oma_resi_bot.utils.signal_handler import register_termination_callback


def _get_updater_and_dispatcher(telegram_token: str) -> Tuple[Updater, Dispatcher]:
    """
    Generates a fresh telegram updater and dispatcher
    :param telegram_token: Your telegram bot token
    :return: updeter and dispatcher
    """
    updater_ = Updater(telegram_token)
    return updater_, updater_.dispatcher


updater, dispatcher = _get_updater_and_dispatcher(config.bot_token)


def start():
    """
    Starts the telegram bot
    """
    global updater
    logger.info("Starting to poll updates for telegram")
    updater.start_polling()


def stop():
    """
    Stops the telegram bot
    """
    global updater
    logger.info("Gracefully shutting down telegram bot...")
    updater.stop()
    logger.info("...telegram bot shut down")


register_termination_callback(stop)
