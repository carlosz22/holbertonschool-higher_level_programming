#!/usr/bin/python3
"""
Module: `2-is_same_class.py`
"""


def is_same_class(obj, a_class):
    """Checks if an object is exactly an instance of a class"""
    return type(obj) is a_class
