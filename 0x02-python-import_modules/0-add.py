#!/usr/bin/python3

'''
Imports the function  def add(a, b): from the file add_0.py
and prints the result of the addition 1 + 2 = 3

    *uses print function with string format to display integers
    * The program is not executed when imported - by uding __import__
'''
if __name__ == "__main__":
    from add_0 import add
    
    a = 1
    b = 2

    result = add(a,b)
    print(f"{a} + {b} = {result}")
