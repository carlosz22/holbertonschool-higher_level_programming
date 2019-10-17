#!/usr/bin/python3
import json
"""
Module: `6-from_json_string.py`
"""


def from_json_string(my_obj):
    """Returns an object represented by a JSON string"""
    return json.loads(my_obj)
