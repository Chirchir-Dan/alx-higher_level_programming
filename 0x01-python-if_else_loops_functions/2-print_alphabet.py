#!/usr/bin/python3
# Prints ASCII alohabet in lowercase
# Excluding 'q' and 'e' not followed by a new line
print(''.join(chr(i) for i in range(97, 123) if i not in (101, 113)), end='')
