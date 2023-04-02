#!/usr/bin/python3
"""Takes a URL,sends a request to it and displays value of x-Request-Id var."""

import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(resonse.headers).get("X-Request-Id"))
