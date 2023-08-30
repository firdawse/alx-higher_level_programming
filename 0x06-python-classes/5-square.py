#!/usr/bin/python3

"""Square Class"""


class Square:
    """Represent a Square"""

    def __init__(self, size=0):
        """
        Args:
            self: used to initiate Square instances
            size (int): size of Square
        """
        self.__size = size

    @property
    def size(self):
        """ current size of the square."""
        return self.__size

    @size.setter
    def size(self, size):
        """
        Sets the size of the Square 
        Args:
            size (int): size of Square 
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size


    def area(self):
        """
        Return: area of Square
        """
        return self.__size * self.__size

    def my_print(self):
        """square in # """
        if self.__size == 0:
            print()

        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
