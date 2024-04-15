#!/usr/bin/python3

"""
This module contains a function to lookup attributes and methods of an object
"""


def lookup(obj):
    """
    Return a list of variable attributes and methods of a n object.
    Args:
    obj: The object to look up attributes and method for.
    Returns:
    A list containing the names of attributes and methods of the object
    """

    return dir(obj)
