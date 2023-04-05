#!/usr/bin/python3
"""
script that fetches an url using the requests package
"""
import requests

if __name__ == "__main__":
    req = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:\n\t- type: {}".format(type(req.text)))
    print("\t- content: {}".format(req.text))
