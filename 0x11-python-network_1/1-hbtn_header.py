#!/usr/bin/python3
"""
Displays the X-Request-Id header from an HTTP response
"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        data = response.read()
        print(response.getheader('X-Request-Id'))
