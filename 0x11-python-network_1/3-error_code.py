#!/usr/bin/python3
"""takes in a URL, sends a request & displays the value of
the X-Request-Id VAR found in header
"""

from urllib import request
from urllib import error
import sys

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
                body = response.read()
                print(body.decode('utf-8'))
                except error.HTTPError as error:
                print('Error code: {}'.format(error.code))
