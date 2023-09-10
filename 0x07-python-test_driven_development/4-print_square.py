#!/usr/bin/python3
"""function that prints squares"""


def print_square(size):
    """function that prints squares using '#' 
    Raises:
        TypeError: if size is not an integer or
                    if size  float and less than 0,
        ValueError: if size == 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        if isinstance(size, float):
            raise TypeError("size must be an integer")
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()

