#!/usr/bin/python3
"""Defines a class Square"""

class Square:
    """
    Class that defines properties of square.
    """
    def __init__(self, size=0):
        """Creates new instances of square.
        """
        self.__size = size

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        """Returns the size of a square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Property setter for size.
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
