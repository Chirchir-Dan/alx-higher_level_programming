#!/usr/bin/python3

""" Prints x elements of a list and skips other value types silently"""


def safe_print_list_integers(my_list=[], x=0):
    """
    Prints integers on the same line
    raises exception if x is bigger than length of my_list

    Parameters:
    my_list (list): list to print elements from.
    X (int): The number of elements to print.

    Return:
    int: The number of integers printed
    """

    count = 0

    try:
        for i in range(x):
            try:
                value = int(my_list[i])
                print("{:d}".format(my_list[i]), end="")
                count += 1
            except (ValueError, TypeError):
                continue
    except IndexError:
        pass
    else:
        print()
        return count
    raise IndexError("list index out of range")
