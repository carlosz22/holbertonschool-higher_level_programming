#!/usr/bin/python3
"""
Displays the X-Request-Id header from an HTTP response
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.get(url)
    data = req.text
    print(req.headers.get('X-Request-Id'))
