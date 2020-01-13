#!/usr/bin/python3
"""
Returns a formatted response using urllib
"""
import requests


req = requests.get('https://intranet.hbtn.io/status')
data = req.text
data_type = type(data)

print("Body response:")
print("\t- type: {}".format(data_type))
print("\t- content: {}".format(data))
