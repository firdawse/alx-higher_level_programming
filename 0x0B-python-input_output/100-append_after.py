#!/usr/bin/python3
"""Defines an append after function"""


def append_after(filename="", search_string="", new_string=""):
    """
    Insert a line of text into a file after each line containing a specific string.

    Returns: None
    """
    with open(filename, 'r+') as file:
        lines = file.readlines()  

        for i, line in enumerate(lines):
            if search_string in line:
                lines.insert(i + 1, new_string)

        file.seek(0)
        file.truncate()
        file.writelines(lines)


