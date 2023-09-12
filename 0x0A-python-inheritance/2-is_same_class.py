#!/usr/bin/python3
"""check Class Type"""


def is_same_class(obj, a_class):
    """returns True if the object is exactly an instance of class"""

    return True if type(obj) == a_class else False
