#!/usr/bin/python3
"""
"""
import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]

    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
    req = requests.get(url)
    data = req.json()
    for i in range(10):
        print(data[i].get('sha'), end=': ')
        print(data[i].get('commit').get('author').get('name'))
