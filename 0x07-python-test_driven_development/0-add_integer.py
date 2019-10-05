#!/usr/bin/python3
"""
Module: `0-add_integer.py`

This module contains the following implementation of functions or classes:

add_integer
"""

def add_integer(a, b=98):
    """ Function: `add_integer` - Add two numbers (int or float)
    Args: a: int or float, b: int or float
    Return: On success, the integer of the addition of the two numbers
    """
    if isinstance(a, int) or isinstance(a, float):
        a = int(a)
    else:
        raise TypeError('a must be an integer')

    if isinstance(b, int) or isinstance(b, float):
        b = int(b)
    else:
        raise TypeError('b must be an integer')

    return a + b
