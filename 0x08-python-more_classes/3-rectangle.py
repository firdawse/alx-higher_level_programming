#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle:
    """rectangle class"""

    def __init__(self, width=0, height=0):
        """rectangle class
        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieve width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height attribute"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    
    def area(self):
        """area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
    
    def __str__(self) -> str:
        """diagram of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = ""
        for col in range(self.__height):
            for row in range(self.__width):
                rect += "#"
            if col < self.__height - 1:
                rect += "\n"
        return rect
