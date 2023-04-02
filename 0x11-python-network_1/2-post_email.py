#!/usr/bin/python3
"""sends a POST request to the passed URL with the emails as parameter
   Displays the body of the response.
"""

import sys
import.urllib.request

if __name__== "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urllencode(value).encode("ascii")

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8")