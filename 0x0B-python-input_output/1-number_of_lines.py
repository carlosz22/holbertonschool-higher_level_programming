#!/usr/bin/python3
"""
Module: `1-number_of_lines.py`
"""


def number_of_lines(filename=""):
    """Returns the number of lines of a text file"""
    with open(filename, 'r', encoding="utf-8") as f:
        line_number = 0
        for line in f:
            line_number += 1
    return line_number
