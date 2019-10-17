#!/usr/bin/python3
import json
"""
Module: `7-save_to_json_file.py`
"""


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using a JSON representation"""
    with open(filename, 'w', encoding="utf-8") as f:
        string = json.dumps(my_obj)
        f.write(string)
