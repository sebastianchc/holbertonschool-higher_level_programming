#!/usr/bin/python3
from requests import post
from sys import argv


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if argv == 1:
        print("No result")
        return
    try:
        request = post(url, {"q": argv[1]})
        js = request.json()
        if not js:
            print("No result")
        else:
            print("[{}] {}" .format(js.get("id"), js.get("name")))
    except:
        print("Not a valid JSON")
