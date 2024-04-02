#!/usr/bin/python3

""" This module contains a function for printing elements of a list safely"""


def safe_print_list(my_list=[], x=0):
    """
    Prints x elements of a list safely.
    it iterates through the list and prints upto the specified
    number of elements.

    Parameters:
    my_list (list): The list to print elements from.
    X (int): The number of elements printed.
    """

    # Keeps track of number of elements printed.
    count = 0

    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            count += 1
    except IndexError:
        pass

    print()
    return count
