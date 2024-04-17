#!/usr/bin/python3
"""
This module provides a function that checks if an object is an
instance of a class or is an instance of a child of the specified
class
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of a class or its child.
    Args:
        obj: The object to be checked
        a_class: The class to be checked against
    Returns:
         True if obj is an instance og a_class or its subclass.
         False otherwise
    """

    return isinstance(obj, a_class)
