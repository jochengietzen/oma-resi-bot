"""
Main module of oma_resi_bot
"""
from oma_resi_bot.telegram_handler.bot import dispatcher, start
from oma_resi_bot.telegram_handler.message_handler import register_handler
from oma_resi_bot.utils.logger import logger


def main():
    """Main function"""
    logger.info("Register handlers")
    register_handler(dispatcher)
    logger.info("Dispatcher configured...")


if __name__ == "__main__":
    main()
    start()
