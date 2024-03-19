#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Extracting the first two elements from each tuple or using 0
    a = tuple_a[:2] + (0, 0)
    b = tuple_b[:2] + (0, 0)

    # Summing up corresponding elements from both tuples
    result = (a[0] + b[0], a[1] + b[1])

    return result
