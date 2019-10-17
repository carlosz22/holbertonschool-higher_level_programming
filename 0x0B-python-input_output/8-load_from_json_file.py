#!/usr/bin/python3
import json
"""
Module: `8-load_from_json_file.py`
"""


def load_from_json_file(filename):
    """Creates an object from a JSON file"""
    with open(filename, 'r', encoding="utf-8") as f:
        string = f.read()
        object = json.loads(string)
        return object
