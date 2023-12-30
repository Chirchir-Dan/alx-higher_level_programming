#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0

    try:
        for i in range(x):
            if type(my_list[i]) == int:
                print("{:d}".format(my_list[i]), end="")
                count += 1
        print()  # Add a new line after printing all integers
    except (IndexError, TypeError) as e:
        import traceback
        traceback_str = traceback.format_exc()
        print(traceback_str, end="")

    return count
