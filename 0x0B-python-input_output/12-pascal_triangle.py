#!/usr/bin/python3
"""Defines a pascal triancle function"""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.
    Returns: list representation of the triangle
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        temp = [1]
        row = triangle[-1]  

        for j in range(1, i):
            new_value = row[j - 1] + row[j]
            temp.append(new_value)

        temp.append(1)
        triangle.append(temp)

    return triangle

