#!/usr/bin/python3

def search_replace(my_list, search, replace):
    # Create a new list with the same elements as the initial list
    new_list = my_list[:]

    for i in range(len(new_list)):
        if new_list[i] == search:
            new_list[i] = replace

    return new_list
