import pytest

from tests.test_telegram.messages import TestMessage, test_messages


@pytest.fixture
def mocked_test_messages():
    return {k: TestMessage(**v) for k, v in test_messages.items()}
