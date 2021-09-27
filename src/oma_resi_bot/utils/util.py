"""
Utility funcitons module
"""
import random
import string


def random_string(length_: int) -> str:
    """
    Generates a random string of length length_
    :param length_: The random string length_
    :return: A random string
    """
    return "".join(
        random.SystemRandom().choice(string.ascii_lowercase + string.digits)
        for _ in range(length_)
    )
