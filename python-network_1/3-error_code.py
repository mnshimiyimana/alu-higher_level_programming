#!/usr/bin/python3
"""displays the body of the response"""

import urllib.request
import urllib.error
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
        except urllib.error.URLError as e:
            print("Error code: {}".format(e.reason))
