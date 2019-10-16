#!/usr/bin/python3
"""
Module: `101-add_attribute.py`
"""


def add_attribute(obj, name, value):
    """Check if it is possible to add an attribute to a class
    and then if yes add it"""
    if "__dict__" not in dir(obj):
        raise TypeError("can't add new attribute")

    setattr(obj, name, value)
