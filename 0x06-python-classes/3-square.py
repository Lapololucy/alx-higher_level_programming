#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    A square class with a private object attribute.
    Checks the type of the argument and raises an exception on error
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    """
    Returns the area of the square
    """
    def area(self):
        return self.__size ** 2
