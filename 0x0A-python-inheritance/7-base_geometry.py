#!/usr/bin/python3
"""
This module provides two classes area and integer_validator
"""


class BaseGeometry:
    """
    class BaseGeometry
    """

    def area(self):
        """
        raises an Exception
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value

        Args:
            name (str): name of the value to be validated.
            value (int): value to be validated

        Raises:
            TypeError: If the value is not an integer
            ValueError: If the value is <= 0
        """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
