#!/usr/bin/python3
"""afend text to the end of the filen"""


def append_write(filename="", text=""):
    """Appends a string to the end of txt file.
    Returns: nbr of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
