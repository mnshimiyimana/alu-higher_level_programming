#!/usr/bin/python3
"""Solve multiple technical challenges"""

from requests import get, auth
import sys

if __name__ == '__main__':
    try:
        repo = sys.argv[1]
        owner = sys.argv[2]
        url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
        r = get(url)
        json = r.json()
        for i in range(10):
            print("{}: {}".format(json[i].get('sha'),
                                  json[i].get('commit').get('author').get('name')))
    except:
        print("None")

