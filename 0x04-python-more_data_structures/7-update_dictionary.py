#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value

    # Return the sorted dictionary
    sorted_dict = dict(sorted(a_dictionary.items()))
    return sorted_dict
