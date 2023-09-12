#!/usr/bin/python3
"""reads txt file"""


def read_file(filename=""):
    """reads a txt file and
    Prints it to stdout
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
