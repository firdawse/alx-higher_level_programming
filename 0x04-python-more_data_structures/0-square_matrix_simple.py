#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if len(matrix) == 0:
        return matrix
    else:
        new_matrix = []
        for i in range(len(matrix)):
            new_matrix.append(list(map(lambda x: x * x, matrix[i])))
        return new_matrix
