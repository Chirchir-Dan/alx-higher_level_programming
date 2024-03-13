#!/usr/bin/python3
# Prints a string in uppercase followed by a new line.

def uppercase(string):
    result = ''
    for char in string:
        if ord('a') <= ord(char) <= ord('z'):
            uppercase_char = chr(ord(char) - 32)
            result += "{}".format(uppercase_char)
        else:
            result += "{}".format(char)
    print(result)
