#!/usr/bin/python3
""" Divides 2 integers and prints the result"""


def safe_print_division(a, b):
    """
    Divides 2 integers and prints the result

    Arguments:
    a,b: integers to be divided.

    Return:
    value of the division, otherwise None.
    """

    try:
        result = a/b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
        return result
