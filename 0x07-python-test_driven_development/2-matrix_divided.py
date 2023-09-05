#!/usr/bin/python3
"""function to divide a matrix to a number"""


def matrix_divided(matrix, div):
    """New matrix divided by div is returned"""

    # case of non-number div
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    # case of div == 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Check that items lists
    if sum([not isinstance(item, list) for item in matrix]) != 0:
        raise TypeError("matrix must be a lists of integers/floats")

    # case of different length list
    length = len(matrix[0])
    for row in matrix:
        if len(row) != length:
            raise TypeError("rows must have the same size")

    # case of non number element in the matrix 
    for row in matrix:
        if sum([not isinstance(value, (int, float)) for value in row]) != 0:
            raise TypeError("matrix must be lists of integers pr floats")

    # Divide the matrix
    new_matrix = []
    for row in matrix:
        new_row = []
        for value in row:
            new_row.append(round(value / div, 2))
        new_matrix.append(new_row)

    return new_matrix
