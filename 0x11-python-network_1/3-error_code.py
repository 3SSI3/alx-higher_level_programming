#!/usr/bin/python3
"""takes in a URL, sends a request & displays the value of
the X-Request-Id VAR found in header
"""

from urllib import request
from urllib import error
from sys import argv

if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except error.HTTPError as er:
        print('Error code: {}'.format(er.code))
