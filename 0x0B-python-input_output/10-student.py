#!/usr/bin/python3
"""Class that defines a Student"""


class Student:
    """class that represents a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrives dictionary representation"""

        if (type(attrs) == list and
                all(type(e) == str for e in attrs)):
            return {key: getattr(self, key) for key in attrs if hasattr(self, keu)}
        return self.__dict__
