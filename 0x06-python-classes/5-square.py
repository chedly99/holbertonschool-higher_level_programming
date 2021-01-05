#!/usr/bin/python3
"""
Square module.
"""


class Square:
    """
    Square
    """
    def __init__(self, size=0):
        """
        Initilise the instance attribut
        Args:
            size (int): the size of the square
        """
        self.__size = size

    @property
    def size(self):
        """
        Getter of instance attributes
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter of instance attributes
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Area returns the current square area
        """
        return self.__size**2

    def my_print(self):
        """
        documentation of the methode my_print
        """
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end='')
            print("")

        if self.__size == 0:
            print("")
            return
