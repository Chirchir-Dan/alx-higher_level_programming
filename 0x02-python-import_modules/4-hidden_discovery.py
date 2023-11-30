#!/usr/bin/python3.8
import sys
import traceback

if __name__ == "__main__":
    try:
        # Import the compiled module
        compiled_module = __import__('hidden_4')

        # Print names in alphabetical order that do not start with '__'
        for name in sorted(dir(compiled_module)):
            if not name.startswith('__'):
                print(name)
    except Exception as e:
        traceback.print_exc()
        sys.exit("An error occurred during module import.")
