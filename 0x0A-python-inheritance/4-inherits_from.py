#!/usr/bin/python3
"""Defines an inherited class-cheking function."""


def inherits_from(obj, a_class):
    """Checks if an object is a inherited instance of a class."""
    if issubclass(type(obj), a_class) and (type(obj) != a_class:
            return True
    return False
