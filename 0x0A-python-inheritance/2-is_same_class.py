#!/usr/bin/python3
"""Module 2-is_same_class
"""


def is_same_class(obj, a_class):
    """Checks if an object is an instance of a class
    Args:
        obj (_object): _description_
        a_class (class): _description_
    Returns:
        True: if object is an instance of class
        False: if it is not
    """

    return True if type(obj) is a_class else False
