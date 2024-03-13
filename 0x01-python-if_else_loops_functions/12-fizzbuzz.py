#!/usr/bin/python3
# Prints the numbers 1 to 100 separated by a space and prints:
# Fizz instead of multiples of 3
# Buzz instead of multiples of 5
# FizzBuzz instead of multiples of both 3 and 5.
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")
