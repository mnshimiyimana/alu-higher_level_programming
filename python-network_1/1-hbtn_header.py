#!/usr/bin/python3
"""Create a Python script that sends a request to the URL."""


import sys
import urllib.request


if __name__ == '__main__':
    with urllib.request.urlopen(sys.argv[1]) as response:
        headers = response.info()
        print(headers['X-Request-Id'])