#!/usr/bin/python3
"""checks if the object is an instance of a class"""

def is_same_class(obj, a_class):
    """function that determines if obj is an exact instanceof a class"""
    if type(obj) is a_class:
        return True
    return False
