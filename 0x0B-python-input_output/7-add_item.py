#!/usr/bin/python3

import sys

save_file = __import__('5-save_to_json_file').save_to_json_file
load_obj = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv[1:]

# Load the existing List or initialize an empty list
items_list = load_obj("add_item.json") if args else []

items_list.extend(args)

save_file(items_list, "add_item.json")
