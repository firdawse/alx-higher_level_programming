#!/usr/bin/python3
"""Base module"""

import json
import os

class Base:
    """this is the main class"""

    __nb_objects = 0

    def __init__(self, _id=None):
        """private attributes
            Args:
                _id (int): A integer
        """
        if _id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = _id
    
