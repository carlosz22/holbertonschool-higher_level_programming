#!/usr/bin/python3
"""
Module: `2-read_lines.py`
"""


def read_lines(filename="", nb_lines=0):
    """Reads n lines of a text file and prints it to stdout"""
    with open(filename, 'r', encoding="utf-8") as f:
        line_number = 0

        while True:

            line = f.readline()

            if not line:
                break

            line_number += 1

            print(line, end='')

            if line_number >= nb_lines and nb_lines > 0:
                break
