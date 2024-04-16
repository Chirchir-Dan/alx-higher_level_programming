#!/usr/bin/python3
""" This module defines a class square"""


class Square:
    """
    A class to represent a square.
    """

    def __init__(self, size=0):
        """
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Computes and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
