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

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation"""
        if json_string is None:
            return []
        return json.loads(json_string)    

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_obj"""
        if list_objs is None:
            list_objs = []

        filename = "{}.json".format(cls.__name__)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string([o.to_dictionary() for o in list_objs]))

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        inst = cls(1, 1)
        inst.x = 0
        inst.y = 0
        inst.update(**dictionary)
        return inst
 
    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = "{}.json".format(cls.__name__)

        if not os.path.exists(filename):
            return []

        instList = []
        with open(filename, "r", encoding="utf-8") as f:
            list_dicts = cls.from_json_string(f.read())
            instList = [cls.create(**e) for e in list_dicts]
        return instList

    @classmethod
    def load_from_file_csv(cls):
        """deserializes CSV"""
        filename = "{}.csv".format(cls.__name__)

        if not os.path.exists(filename):
            return []

        objList = []
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                argums = line[:-1].split(",")
                obj = cls(1, 1)
                obj.update(*[int(x) for x in argums])
                objList.append(obj)
        return objList 
