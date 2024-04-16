#!/usr/bin/python3
"""
This module provides a function that reads a text file and prints itto stdout
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout

    Args:
        filename (str): name of the file to read from
    Returns:
        A list of text.
    """

    with open(filename, encoding="utf-8") as f:
        content = f.read()
        print(content)
