#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

# Get the last digit of the number with the correct sign
last_digit = int(str(number)[-1])

# Determine and print the properties of the last digit
output = f"Last digit of {number} is {last_digit}"

if number < 0:
    output += f" and is less than 6 and not 0" if last_digit < 0 else ""
elif abs(last_digit) > 5:
    output += " and is greater than 5"
elif last_digit == 0:
    output += " and is 0"

print(output)

