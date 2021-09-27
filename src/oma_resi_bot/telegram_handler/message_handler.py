"""
Message handling for telegram bot
"""
from telegram.ext import CallbackContext, Filters, MessageHandler
from telegram.message import Message as TMessage
from telegram.update import Update

from oma_resi_bot.models.messaging import Message
from oma_resi_bot.utils.logger import logger


def general_message(message_: TMessage):
    """
    This is a handler for all message types
    :param message_: Telegram message
    """
    print(message_)
    content = message_.to_dict()
    print(content)
    message = Message.from_mesage_dict(content)
    print(message)


def photo_message(message_: TMessage):
    """
    This is a handler for photo messages
    :param message_: Telegram message
    """
    content = message_.to_dict()
    print(content)
    # message = MessengerMessage(
    #     message_id=__id_prefix(message_.message_id),
    #     original_message=content,
    #     message_type=MessengerMessageType.PHOTO,
    # )
    # message.type_specific_content = [
    #     photo.get_file().to_dict() for photo in message_.photo
    # ]
    # client_.publish(topic=f"{PUBLISH_TOPIC_BASE}/photo", message=message)


def all_messages(update: Update, _: CallbackContext) -> None:
    """
    This function will handle the different message handlers
    :param update: Telegram update object
    :param _: Callback Context
    """
    matched = False
    message = update.message
    logger.info("Received message ...")
    logger.debug(message.to_dict())
    if Filters.command.filter(message):
        logger.info("\t... of type command")
        matched = True
        general_message(message)
    if Filters.photo.filter(message):
        logger.info("\t... of type photo")
        matched = True
        photo_message(message)
    if Filters.text.filter(message):
        logger.info("\t... of type text")
        matched = True
        general_message(message)
    if Filters.all.filter(message) and not matched:
        logger.info("\t... did not match any filters!")
        general_message(message)


def register_handler(dispatcher_):
    """
    This function registers your message handlers
    :param dispatcher_: The dispatcher to handle your messages
    """
    dispatcher_.add_handler(MessageHandler(Filters.all, all_messages))
