#!/usr/bin/python3
"""
DIsplays the X-Request-Id header from an HTTP response
"""
import urllib.request
import sys


url = sys.argv[1]
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    data = response.read()
print(response.getheader('X-Request-Id'))
