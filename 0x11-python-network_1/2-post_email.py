#!/usr/bin/python3
"""
Sends a POST request with a parameter
"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    url_param = {'email': email}

    data = urllib.parse.urlencode(url_param)
    data = data.encode('utf8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf8'))
