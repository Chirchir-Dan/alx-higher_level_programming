#!/usr/bin/python3
import importlib

if __name__ == "__main__":
    module_name = 'variable_load_5'
    variable_name = 'a'

    try:
        module = importlib.import_module(module_name)
        if hasattr(module, variable_name):
            a_value = getattr(module, variable_name)
            print(a_value)
        else:
            print("Variable 'a' not found in the module.")
    except ImportError:
        print(f"Error importing module '{module_name}'.")
