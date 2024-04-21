#!/usr/bin/python3
"""
This module provides a class Square that inherits from class Rectangle.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Inherits from Rectangle class.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor for Square class.

        Args:
            size (int): The size of the square.
            x (int, optional): The x-coordinate of the square.
                Defaults to 0.
            y (int, optional): The y-coordinate of the square.
                Defaults to 0.
            id (int, optional): The id of the square.
                Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        String representation of the Square instance.

        Returns:
            str: [Square] (<id>) <x>/<y> - <size>
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
