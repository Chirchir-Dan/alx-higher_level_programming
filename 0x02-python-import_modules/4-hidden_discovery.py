#!/usr/bin/python3
if __name__ == "__main__":
    names = [name for name in dir(hidden_4) if not name.startswith('__')]
    names.sort()

    for name in names:
        print(name)
