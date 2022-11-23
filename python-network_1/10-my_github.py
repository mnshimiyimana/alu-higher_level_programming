#!/usr/bin/python3
"""takes my Github credentials (username and password) and uses the Github API to display your id"""



from requests.auth import get, auth
import sys

if __name__ == '__main__':
    url = 'https://api.github.com/user'
    user = sys.argv[1]
    password = sys.argv[2]
    r = requests.get(url, auth=HTTPBasicAuth(user, password))
    print(r.json().get('id'))
    try:
        print(r.json().get('id'))
    except:
        print("None")
