#!/usr/bin/python3
"""
    documentation of the module square
         1 - Square
"""


class Square:
    """
    documentation of the class Square
        *methodes:
            __init__
            area
        *attributes:
            size: private
    """
    def __init__(self, size=0):
        """documentation of the method __init__: constructor"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """documentation of the method area: return the area of square"""
        return self.__size**2
