#!/usr/bin/python3

"""Square Class"""


class Square:
    """one private attribute"""

    __size = 0

    def __init__(self, size):
        """
        Args:
            self: used to initiate Square instances
            size (int): size of Square
        """
        self.__size = size
