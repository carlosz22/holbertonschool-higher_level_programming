#!/usr/bin/python3
"""
"""


def matrix_divided(matrix, div):
    """
    """
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError('div must be a number')
    elif div == 0:
        raise ZeroDivisionError('division by zero')

    if len(matrix) == 0:
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

    new_matrix = []

    size = len(matrix[0])

    for i in range(len(matrix)):

        if not isinstance(matrix[i], list):
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
        elif size != len(matrix[i]):
            raise TypeError('Each row of the matrix must have the same size')

        size = len(matrix[i])

        new_matrix.append([])

        for j in range(len(matrix[i])):

            if not isinstance(matrix[i][j], int) and not isinstance(matrix[i][j], float):
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

            result = matrix[i][j] / div
            result = round(result, 2)
            new_matrix[i].append(result)

    return new_matrix
