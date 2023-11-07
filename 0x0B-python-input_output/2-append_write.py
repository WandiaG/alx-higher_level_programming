#!/usr/bin/python3
"""Module containing the function append_write"""

def append_write(filename="", text=""):
    """"writes the characters added.

    Args:
        filename (str, optional): name of the file. Defaults to "".
        text (str, optional): string of text to write to file. Defaults to "".

    Returns:
        int: number of characters appended to file.
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
