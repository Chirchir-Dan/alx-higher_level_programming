#!/usr/bin/python3
"""
This module provides a class Rectangle that inherits from class Basw
"""


from models.base import Base


class Rectangle(Base):
    """
    inherits from class Base

    Attributes:
        width (int): The width of the rectangle
        height (int): the height of the rectangle
        x (int): The x-coordinate of the rectangle.
        y (int): The y-coordinate of the rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for Rectangle class

        Args:
            width (int)
            height (int)
            x (int, optional):
            y (int, optional)
            id (int, optional): The id of the rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter for the width attribute.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width attribute.

        Args:
            value (int): The width of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for the height attribute.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height attribute.

        Args:
            value (int): The height of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Getter for the x-coordinate attribute.

        Returns:
            int: The x-coordinate of the rectangle.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for the x-coordinate attribute.

        Args:
            value (int): The x-coordinate of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Getter for the y-coordinate attribute.

        Returns:
            int: The y-coordinate of the rectangle.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for the y-coordinate attribute.

        Args:
            value (int): The y-coordinate of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        Displays the Rectangle instance with the character #
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " *self.x + "#" * self.width)

    def __str__(self):
        """
        String representation of the Rectangle instance.

        Returns:
            str: [Rectangle] (<id>) <x>/<y> - <width>/<height>/<height>
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height))

    def update(self, *args):
        """
        Assigns arguments to each attribute.

        Args:
            *args: The arguments to assign.
                1st argument: id attribute
                2nd argument: width attribute
                3rd argument: height attribute
                4th argument: x attribute
                5th argument: y attribute
        """
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 3:
            self.height = args[2]
        if len(args) >= 4:
            self.x = args[3]
        if len(args) >= 5:
            self.y = args[4]
