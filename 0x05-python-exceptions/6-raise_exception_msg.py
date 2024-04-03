#!/usr/bin/python3
""" Raises a name exception with a message"""


def raise_exception_msg(message=""):
    """
    Raises a name exception with a custom message.

    Args:
        message(str): The custom message to include in the exception.

    Raises:
        NameError: Always raised with the specified message.
    """

    raise NameError(message)
