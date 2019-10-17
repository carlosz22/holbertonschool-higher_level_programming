#!/usr/bin/python3
"""
Module: `4-append_write.py`
"""


def append_write(filename="", text=""):
    """Appends a string to a file and returns the number of characters"""
    with open(filename, 'a', encoding="utf-8") as f:
        f.write(text)

    return len(text)
