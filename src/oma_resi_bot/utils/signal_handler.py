"""
Basic signal handling module
"""
# pylint: disable=global-variable-not-assigned
import signal
from typing import Callable

from oma_resi_bot.utils.logger import logger

FUNCTIONS = {}


def register_termination_callback(function: Callable):
    """
    Registers a termination callback
    :param function: a function to be executed
    """
    global FUNCTIONS

    logger.info("Registering signal shutdowns for %s", function.__name__)

    if function.__name__ in FUNCTIONS:
        raise ValueError("Duplicate function registration not allowed!")

    FUNCTIONS[function.__name__] = function


# pylint: disable=unused-argument,global-variable-not-assigned
def __shutdown_after_signal(*args, **kwargs):
    """
    This function allows you to execute your function at shutdown time
    :param args: args
    :param kwargs: kwargs
    """
    global FUNCTIONS

    for fun_name, fun in FUNCTIONS.items():
        logger.info("Shutting down by executing %s", fun_name)
        fun()


signal.signal(signal.SIGINT, __shutdown_after_signal)
signal.signal(signal.SIGTERM, __shutdown_after_signal)
