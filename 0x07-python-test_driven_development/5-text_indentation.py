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

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for delim in ".?:":
        text = (delim +"\n\n").join(
                [line.strip(" ") for line in text.split(delim)]
                )
    print("{}".format(text), end="")
