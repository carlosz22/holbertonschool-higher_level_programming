#!/usr/bin/python3
"""
Module: `3-is_kind_of_class.py`
"""


def inherits_from(obj, a_class):
    """Checks if an object is an instance of, or inherited from a class"""
    return isinstance(obj, a_class) and type(obj) is not a_class
