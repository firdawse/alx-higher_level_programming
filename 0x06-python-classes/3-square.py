#!/usr/bin/python3

"""Square Class"""


class Square:
    """Square attributesand methods"""

    __size = 0

    def __init__(self, size=0):
        """
        Args:
            self: used to initiate Square instances
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
        return pow(self.size, 2)

