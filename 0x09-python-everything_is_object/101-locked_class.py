#!/usr/bin/python3
"""locked class"""


class LockedClass:
    """
    Prevent the user from instantiating new attribute except for  "first_name"
    """

    __slots__ = ["first_name"]
