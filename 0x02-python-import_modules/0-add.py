#!/usr/bin/python3
from add_0 import add
'''
Imports the function  def add(a, b): from the file add_0.py
and prints the result of the addition 1 + 2 = 3

    *uses print function with string format to display integers
    * The program is not executed when imported - by uding __import__
'''
if __name__ == "__main__":
    
    a = 1
    b = 2
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
