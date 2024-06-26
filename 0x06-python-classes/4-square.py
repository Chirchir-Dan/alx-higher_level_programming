#!/usr/bin/python3
""" This module defines a class square"""


class Square:
    """
    A class to represent a square.
    """

    def __init__(self, size=0):
        """Initializes the square with the given size.

        Args:
            size (int, optional): The size of the square, defaults to 0.
        """

        self.size = size

    @property
    def size(self):
        """"Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Computes and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
