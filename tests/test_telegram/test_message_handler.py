import pytest

from oma_resi_bot.models.messaging import Message
from oma_resi_bot.telegram_handler.message_handler import general_message


def test_general_message(mocked_test_messages):
    general_message(mocked_test_messages["another_time"])


def test_message_parsing(mocked_test_messages):
    msg = Message.from_mesage_dict(mocked_test_messages["another_time"])
    assert msg.sender.id == str(mocked_test_messages["another_time"]["from"]["id"])
