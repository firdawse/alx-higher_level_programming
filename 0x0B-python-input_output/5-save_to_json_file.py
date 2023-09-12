#!/usr/bin/python3
"""writes an Object to a JSON file"""


import json


def save_to_json_file(my_obj, filename):
    """Accepts anobject and sends JSON representation to filename"""

    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
