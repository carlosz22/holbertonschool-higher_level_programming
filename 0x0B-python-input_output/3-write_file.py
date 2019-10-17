#!/usr/bin/python3
"""
Module: `3-write_file.py`
"""


def write_file(filename="", text=""):
    """Writes a string to a file and returns the number of characters"""
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)

    return len(text)
