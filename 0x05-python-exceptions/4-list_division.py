#!/usr/bin/python3
""" Divides elements of two lists"""


def list_division(my_list_1, my_list_2, list_length):
    """
    Takes 2 lists as input and divides element by element.

    Parameters:
    my_list_1 (list): The first list.
    my_list_2 (list): The second list.
    list_lenght (int): The desired length of the resulting list.

    Return:
    list: A new list (length = list_length) with all divisions.
    """

    new_list = []

    for i in range(list_length):
        try:
            division = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            division = 0
        except ZeroDivisionError:
            print("division by 0")
            division = 0
        except IndexError:
            print("out of range")
            division = 0
        finally:
            new_list.append(division)
    return new_list
