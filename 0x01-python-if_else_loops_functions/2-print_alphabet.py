#!/usr/bin/python3
# Prints ASCII alohabet in lowercase
# Excluding 'q' and 'e' not followed by a new line
for i in range(97, 123):
    if chr(i) not in ['q', 'e']:
        print(chr(i), end='')
