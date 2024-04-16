#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    num_args = len(argv) - 1
    arg_list = argv[1:]

    if num_args == 0:
        print("0 arguments.")
    else:
        print(f"{num_args} argument{'s' if num_args != 1 else ''}:")
    for i, arg in enumerate(arg_list, 1):
        print("{}: {}".format(i, arg))
