#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    is_int = True
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as err:
        is_int = False
        print(f"Exception: {err}", file=sys.stderr)
    return is_int
