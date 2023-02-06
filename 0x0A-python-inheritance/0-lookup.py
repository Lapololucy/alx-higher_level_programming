#!/usr/bin/python3
"""Module 0-lookup
Returns a list of the attributes and methods of an object
"""


def lookup(obj):
    """Returns the list of the attributes and methods of obj
    Args:
        obj (_type_): an object to be used
    Returns:
        dir(obj)
    """
    return dir(obj)
