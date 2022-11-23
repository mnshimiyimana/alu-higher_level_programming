#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request """



import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    data = {"q": ""}

    try:
        data["q"] = sys.argv[1]
    except:
        pass

    response = requests.post(url, data)

    try:
        json_0 = response.json()
        if not json_0:
            print("No result")
        else:
            print("[{}] {}".format(json_0.get("id"), json_0.get("name")))
    except:
        print("Not a valid JSON")
