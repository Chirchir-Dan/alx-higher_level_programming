#!/usr/bin/python3
# Prints the last digit of a number

def print_last_digit(number):
    number = abs(number)
    last_digit = number % 10
    print(last_digit)
    return last_digit
