#!/usr/bin/python3
"""
This module provides a function class_to_json that converts an \
object into a dictionary representation suitable for JSON serialization.
"""


def class_to_json(obj):
    """
    Returns a dictionary containing the attributes of an object \
            in a format suitable
    for JSON serialization. The attributes must have simple data \
            types like lists,
    dictionaries, strings, integers, and booleans.

    Args:
        obj (MyClass): The object to convert to a JSON-compatible \
                dictionary.

    Returns:
        dict: A dictionary representation of the object's attributes.
    """

    return obj.__dict__
