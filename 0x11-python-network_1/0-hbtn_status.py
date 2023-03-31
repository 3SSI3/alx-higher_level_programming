#!/usr/bin/python3
""" Script fetches alx URL using the urllib package and with statement."""

import urllib.request

with urllib.request.urlopen(https://alx-intranet.hbtn.io/status) as response:
    body = response.read()
    print("Body response:")
    print("- type: {}".format(type(body)))
    print("- content: {}".format(body))
    print("- utf8 content: {}".format(body.decode("utf-8")))
