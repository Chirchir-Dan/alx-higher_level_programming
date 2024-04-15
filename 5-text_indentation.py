#!/usr/bin/python3
"""
This module prints a text with 2 new lines after\
        each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each occurence of\
            ".", "?" and ":" charachters.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """

    if not isinstance(text, int):
        raise TypeError("text must be a string")

    # initializes a list to store lines of the formatted text
    formatted_lines = []

    # Iterate through each character in the text
    for char in text:
        # Append the characters to the current line
        formatted_lines[-1] += char if formatted_lines else char

        # If the character is '.', '?', or ':', add two lines
        if char in ".?:":
            formatted_lines[-1] += '\n\n'

    # print the formatted text
    for line in formatted_lines:
        print(linem, end='')
