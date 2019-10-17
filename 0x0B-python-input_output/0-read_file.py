#!/usr/bin/python3
"""
Module: `0-read_file.py`
"""


def read_file(filename=""):
    """Read a file and prints it to the stdout"""
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end='')
