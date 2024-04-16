#!/usr/bin/python3
"""
This module provides a function that writes a string to a text file and returns the nunber of characters written
"""


def write_file(filename="", text=""):
    """
    """
    with open(filename, 'w', encoding="utf-8") as file:
        no_chars = file.write(text)
        return no_chars
