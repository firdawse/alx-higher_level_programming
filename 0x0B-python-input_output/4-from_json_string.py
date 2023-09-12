#!/usr/bin/python3
"""transform text to JSON"""

import json


def from_json_string(my_str):
    """Transform a string to JSON file
    Return: json file
    """
    return json.loads(my_str)

