#!/usr/bin/python3
"""

This module provides a function to check if object is an instance \
        of a specified cladd.
"""


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of the specified class;
    Args:
        obj: The object to check.
        a_class: The class to cimpare against return isinstance(obj, a_class)
    Returns:
        True: if the obj is exactly an instance of a_class
        False: otherwise
    """

    return type(obj) is a_class
