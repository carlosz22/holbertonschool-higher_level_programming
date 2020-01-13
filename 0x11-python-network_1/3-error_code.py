#!/usr/bin/python3
"""
Sends a request and shows if there is an HTTP error
"""
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf8'))
    except urllib.error.HTTPError as e:
        print('Error code:', e.code)
