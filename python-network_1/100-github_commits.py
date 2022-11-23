#!/usr/bin/python3
"""Solve multiple technical challenges"""


from requests import get, auth
import sys

if __name__ == "__main__":
    try:
        repo = sys.argv[1]
        owner = sys.argv[2]
        url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
        response = get(url)
        json_0 = response.json()
        for i in range(0, 10):
            print("{}: {}".format(json_0[i].get("sha"), json_0[i]
                                  .get("commit").get("author").get("name")))
    except:
        pass
