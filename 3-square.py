#!/usr/bin/python3
""" This module defines an empty class named square """


class Square:
    """ creating private instance attribute size with conditions """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size**2
