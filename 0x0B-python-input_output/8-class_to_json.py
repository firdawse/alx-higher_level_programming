#!/usr/bin/python3
"""Function that returns dict description with simple data structure"""


def class_to_json(obj):
    """Transform Object into dict
    Return: dictionnary description
    """
    return obj.__dict__
