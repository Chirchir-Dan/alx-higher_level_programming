#!/usr/bin/python3
"""
Module: 8-rectangle

This module contains the definition of the Rectangle class,
which inherits from BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class representing a rectangle shape.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initialize a rectangle with width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        super().__init__()
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return the string representation of the rectangle.

        Returns:
            str: The string representation of the rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"

    def print(self):
        """
        Print the rectangle description.
        """
        print(self.__str__())

    def __dir__(self):
        """
        Override the __dir__() method to customize the list of
        attributes and methods.

        Returns:
            list: List of attributes and methods specific to the
            Rectangle class.
        """
        return [attr for attr in dir(self) if not attr.startswith('_')]
