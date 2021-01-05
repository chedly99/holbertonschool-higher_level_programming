#!/usr/bin/python3
"""
define a class Square
"""


class Square:
    """sqaure class
    """
    def __init__(self, size=0):

        """square instance"""

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
