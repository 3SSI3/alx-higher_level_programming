#!/usr/bin/python3
class Square:
    """A class that defines a square by its size
    """
    def __init__(self, size=0):
        """Initialize Square Class with size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
