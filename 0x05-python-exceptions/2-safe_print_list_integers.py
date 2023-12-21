#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    print the first x integers from the given list.
    Args:
        my_list (list): The input list.
        x (int): The number of elements to print.

    Returns:
        int: The real number of integers printed.
    """

    count = 0

    try:
        for i in range(x):
            value = my_list[i]
            if type(value) == int:
                print("{:d}".format(value), end=" ")
                count += 1
        print()
    except (TypeError, ValueError, IndexError):
        pass

    return count
