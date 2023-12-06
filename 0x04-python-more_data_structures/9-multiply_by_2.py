#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    # Create a new dictionary with values multiplied by 2
    new_dictionary = {key: value * 2 for key, value in a_dictionary.items()}
    return new_dictionary


if __name__ == "__main__":
    # Example usage:
    my_dictionary = {'a': 1, 'b': 2, 'c': 3}
    result_dictionary = multiply_by_2(my_dictionary)
    print(result_dictionary)
