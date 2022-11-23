#!/usr/bin/python3
"""Create a Python script that fetches a url"""


import requests

if __name__ == '__main__':
    response = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
