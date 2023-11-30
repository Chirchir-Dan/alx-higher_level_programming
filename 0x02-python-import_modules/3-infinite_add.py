#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    # Skip the script name in argv[0]
    arguments = argv[1:]

    # Convert arguments to integers and sum them
    result = sum(int(arg) for arg in arguments)

    print(result)
