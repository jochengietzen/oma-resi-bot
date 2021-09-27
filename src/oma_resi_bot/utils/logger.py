"""
Provides you with a basic logger variable `logger`
"""
import logging
import sys

logger = logging.getLogger("Oma-Resi-Bot")

logger.DEBUG = logging.DEBUG
logger.INFO = logging.INFO
logger.WARNING = logging.WARNING
logger.ERROR = logging.ERROR

LEVEL = logging.INFO

stream_handler = logging.StreamHandler(stream=sys.stdout)
stream_handler.setLevel(LEVEL)

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)8s - %(name)s -   %(message)s",
)
stream_handler.setFormatter(formatter)
logger.setLevel(LEVEL)

logger.addHandler(stream_handler)
