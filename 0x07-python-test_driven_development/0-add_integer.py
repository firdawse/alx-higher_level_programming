#!/usr/bin/python1
"""ADD function

Input are converted into integers 

Raises: TypeError: if any of the arguments is not a number ."""


def add_integer(a, b=98):
    """Return the addition of two numbers"""

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
