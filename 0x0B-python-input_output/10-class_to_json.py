#!/usr/bin/python3
"""
Module: `10-class_to_json.py`
"""


def class_to_json(obj):
    """Dictionary description of a class"""
    if obj.__dict__:
        return obj.__dict__
