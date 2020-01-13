#!/usr/bin/python3
"""
Fetch people from Star Wars API
"""
import requests
import sys


if __name__ == "__main__":
    search_term = sys.argv[1]
    dict_param = {'search': search_term}

    req = requests.get('https://swapi.co/api/people/', params=dict_param)

    data = req.json()

    print("Number of results: {}".format(data.get('count')))

    for character in data.get('results'):
        print(character.get('name'))
