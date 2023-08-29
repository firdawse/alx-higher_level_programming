#!/usr/bin/python3

"""Square Class"""


class Square:
    """one attribute"""
	__size = 0

    def __init__(self,size):
        """
        Args:
            self: used to initiate Square instance
			size: private instance attribute
        """
        self.__size = size
