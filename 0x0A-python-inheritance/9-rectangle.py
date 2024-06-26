#!/usr/bin/python3
"""
Defines a class Rectangle based on 8-base_geometry.py.

Attributes:
    width (int): width of the rectangle.
    height (int): height of the rectangle.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle"""

    def __init__(self, width, height):
        """Creates new instances of Rectangle.

        Args:
            width (int): width of rectangle.
            height (int): height of rectangle.
        """
        super().__init__()
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """Calculates area of a rectangle.

        Returns:
            int: area.
        """
        return self.__width * self.__height

    def __str__(self):
        """Returns string representation of the rectangle.

        Returns:
            str: string representation of rectangle.
        """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)

    def __dir__(self):
        """Customizes the list of attributes and methods.

        Returns:
            list: List of attributes and methods specific to the
            Rectangle class.
        """
        base_attrs = dir(BaseGeometry)
        rectangle_attrs = [attr for attr in dir(self)
                           if not attr.startswith('_')
                           and attr not in base_attrs]
        return rectangle_attrs
