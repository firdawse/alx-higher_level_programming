#!/usr/bin/python3
"""check Class Type"""


def inherits_from(obj, a_class):
    """Check if obj is an instance of a_class or not"""

    return isinstance(obj, a_class) and type(obj) != a_class
