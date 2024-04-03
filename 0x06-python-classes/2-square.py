#!/usr/bin/python3
"""  This module defines the Square class."""


class Square:
    """ A class to represent a square."""

    def __init__(self, size=0):
        """
        Initializes the Square instance wirh the given size.

        Args:
            size (int, optional): The size of the Square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
