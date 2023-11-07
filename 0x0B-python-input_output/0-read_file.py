#!/usr/bin/python3
"""Module containing the function read_file"""

def read_file(filename=""):
    """Reads and prints a file to the stdout.

    Args:
        filename (str, optional): name of file to read. Defaults to "".
    """
    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end='')
