#!/usr/bin/python3

class Square:
    """Class representing a square with a private instance attribute 'size'."""

    def __init__(self, size):
        """Instantiation with a given size.

        Args:
            size (int): The size of the square.

        """
        self.__size = size
