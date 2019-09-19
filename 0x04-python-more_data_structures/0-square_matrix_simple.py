#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    cpy_matrix = matrix[:]
    for i in range(len(cpy_matrix)):
        cpy_matrix[i] = list(map(lambda x: x**2, cpy_matrix[i]))
    return cpy_matrix
