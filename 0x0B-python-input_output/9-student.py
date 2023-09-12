#!/usr/bin/python3
"""Class that defines a Student"""


class Student:
    """class that represents a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation"""
        return self.__dict__
