#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    # Sort the keys in alphabetical order
    sorted_keys = sorted(a_dictionary.keys())

    # Print the dictionary using the sorted keys
    for key in sorted_keys:
        print("{}: {}".format(key, a_dictionary[key]))
