#!/usr/bin/python3
"""
Module: `9-add_item.py`
"""
from sys import argv
import json

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

try:
    json_list = load_from_json_file('add_item.json')
except:
    json_list = list()

for i in range(1, len(argv)):
    json_list.append(argv[i])

save_to_json_file(json_list, 'add_item.json')
