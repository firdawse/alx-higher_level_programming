#!/usr/bin/python3
"""writes string to txt file """


def write_file(filename="", text=""):
    """ Write xtring to textfile
    Return: nbr of characters written
    """
    with open(filename, 'w') as f:
        return f.write(text)
