#!/usr/bin/python3
"""Displays the body of the response"""


import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}
    r = requests.post(url, data)
    print("{}".format(r.text))
