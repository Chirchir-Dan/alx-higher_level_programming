#!/usr/bin/python3
"""
This script adds command-line arguments to a Python list and \
        saves them to a JSON file.

If the file 'add_item.json' exists, it loads the existing list from the file.
If the file doesn't exist, it initializes an empty list.
Then, it appends the command-line arguments to the list.
Finally, it saves the updated list to the file in JSON format.
"""


import sys
save_file = __import__('5-save_to_json_file').save_to_json_file
load_obj = __import__('6-load_from_json_file').load_from_json_file


def add_items_to_list_and_save():
    """
    This method adds command-line arguments to a pyhton list \
    and saves them to a JSON file
    """

    args = sys.argv[1:]

    # Load the existing List or initialize an empty list
    items_list = load_obj("add_item.json") if args else []

    items_list.extend(args)

    save_file(items_list, "add_item.json")


if __name__ == "__main__":
    add_items_to_list_and_save()
