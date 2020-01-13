#!/usr/bin/python3
"""
Get id
"""
import requests
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    req = requests.get('https://api.github.com/user', auth=(user, passwd))
    print(req.json().get('id'))
