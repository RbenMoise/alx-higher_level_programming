#!/usr/bin/python3
"""class of square"""


class Square:
    """const"""
    def __init__(self, size=0):
        """initii"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
