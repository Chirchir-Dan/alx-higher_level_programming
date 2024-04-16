#!/usr/bin/python3
"""
This module provides a function that creates an Object from a \
    "JSON file":
"""


def load_from_json_file(filename):
    """
    Decodes an Object from a JSON file

    Args:
        filename (file): JSON file to create an Object from
    Returns:
        A python Object.
    """

    import json

    with open(filename, encoding="utf-8") as file:
        return json.load(file)
