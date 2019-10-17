#!/usr/bin/python3
"""
Pascal Triangle
"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing the Pascal triangle"""
    if n <= 0:
        return []
    elif n == 1:
        return [[1]]

    this_row = []
    triangle = [[1], [1, 1]]

    for row in range(2, n):
        this_row = [1]
        for column in range(1, row):
            element = triangle[row - 1][column - 1] + triangle[row - 1][column]
            this_row.append(element)
        this_row.append(1)
        triangle.append(this_row)
    return triangle
