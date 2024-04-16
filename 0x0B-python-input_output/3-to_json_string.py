#!/usr/bin/python3
"""
This module provides a function that returns the JSON \
        representation of an object(string):
"""


def to_json_string(my_obj):
    """
    Serializes an object (string)
    Args:
        my_obj (str): The string to be serialized
    Returns:
        The JSON representation of an object.
    """

    import json
    return json.dumps(my_obj)
