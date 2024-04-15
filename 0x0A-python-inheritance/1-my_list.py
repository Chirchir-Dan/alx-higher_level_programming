#!/usr/bin/python3
"""
This module contains the MyList class, a custom list class that inherits from the built-in list class.
"""


class MyList(list):
    """
    A custom list class that inherits from the built-in list class.
    Public methods:
    print_sorted(self): Print the elements of the list sorted in ascending order.
    """
    def print_sorted(self):
        """
        Print the elements of the list sorted in ascending order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
