#!/usr/bin/python3
""" This module provides a function to add two functions. """


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int, float): The first nunber.
        b (int, float, optional): The second number. Defaults to 98.

    Raises:
        TypeError: If either a or b is not an integer or float.

    Returns:
        int: The sum of a and b as an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
