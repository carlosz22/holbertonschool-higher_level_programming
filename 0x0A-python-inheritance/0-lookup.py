#!/usr/bin/python3
"""
Module : `0-lookup.py`

Returns the list of available attributes and methods of an object
"""


def lookup(obj):
    """Function: lookup
       Args:
           obj: Object
       Return:
           list with methods and attributes
    """
    obj_namespace = dir(obj)
    return obj_namespace
