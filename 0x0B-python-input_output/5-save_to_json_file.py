#!/usr/bin/python3
"""
This module provides a function that writes an Object to a txt \
    file, using a JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """
    writes an Object to a text file using a JSON representation
    Args:
        my_obj (python object): object to be written to filename
        filename (file): The file to be written to
    """

    with open(filename, 'w', encoding="utf=8") as file:
        json.dump(my_obj, file)
