#!/usr/bin/python3

"""
Prints an integer and returns True if value is correctly printed
"""


def safe_print_integer(value):
    """
    Prints an integer

    Parameters:
    value: The value to be printed.

    Return:
    bool: True if succesfully printeed as an integer.
    """

    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
