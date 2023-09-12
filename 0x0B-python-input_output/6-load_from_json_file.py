#!/usr/bin/python3
"""create objetcs from json file"""


import json


def load_from_json_file(filename):
    """Create anobject from a JSON file"""
    with open(filename) as f:
        return json.load(f)
