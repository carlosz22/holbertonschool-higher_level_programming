#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    height = len(matrix)
    width = len(matrix[0])
    for i in range(height):
        j = 0
        for j in range(width):
            print("{:d}".format(matrix[i][j]), end='')
            if j < (width - 1):
                print(" ", end='')
        print()
