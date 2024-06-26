#!/usr/bin/python3
"""
This module provides a function that prints a square
"""


def print_square(size):
    """
    The function prints a square with the character #.

    Args:
        size (int): The size length of the square

    Raises:
        TypeError: if size is not an integer or\
                if size is a float and is less than 0.
        ValueError: if size is less than 0.

    Returns:
        None
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
