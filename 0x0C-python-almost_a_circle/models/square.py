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

    @property
    def size(self):
        """
        Getter for the size attribute.

        Returns:
            int: The size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute.

        Args:
            value (int): The size of the square.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Assigns attributes to the instance.

        Args:
        *args: The positional arguments.
            1st argument: id attribute
            2nd argument: size attribute
            3rd argument: x attribute
            4th argument: y attribute
        **kwargs: The keyword arguments.
        Each key represents an attribute.

        Note:
        **kwargs must be skipped if *args exists and is not empty.
        """
        if args:
            attrs = ["id", "size", "x", "y"]
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns a dictionary representation of the Square object.

        Returns:
            dict: A dictionary containing the attributes of the square.
        """
        dict_ = {}
        for key, value in self.__dict__.items():
            clean_key = key.replace("_Rectangle__", "")
            if clean_key == "width" or clean_key == "height":
                dict_["size"] = value
            else:
                dict_[clean_key] = value
        return dict_
