#!/usr/bin/python3
"""
This module provides a function that returns a python object \
        represented by a JSON string
"""

import json


def from_json_string(my_str):
    """
    Decodes a JSON string
    Args:
        my_str (str): A JSON string representing a python object
    Returns:
        object: A python data structure deserialized from JSON string
    """

    return json.loads(my_str)
