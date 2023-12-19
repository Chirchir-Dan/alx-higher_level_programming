#!/usr/bin/python3

class Square:
    """Class representing a square with private instance attribute 'size'."""

    def __init__(self, size=0):
        """Instantiation with optional size.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            int: The area of the square.

        """
        return self.__size ** 2
