#!/usr/bin/python3
def delete_at(my_list=None, idx=0):
    if my_list is None or idx < 0 or idx >= len(my_list):
        return my_list

    new_list = my_list[:idx] + my_list[idx+1:]
    return new_list
