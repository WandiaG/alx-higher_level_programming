#!/usr/bin/python3

def safe_print_integer(value):
    """
    Prints an integer with "{:d}".format().
        Returns: True or false
    """
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError):
        return False
    else:
        return True
