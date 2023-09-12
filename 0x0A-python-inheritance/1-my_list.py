#!/usr/bin/python3
"""inherits lists"""


class MyList(list):
    """contains one fucntion"""

    def print_sorted(self):
        """print a list of sorted ints"""
        print(sorted(self))
