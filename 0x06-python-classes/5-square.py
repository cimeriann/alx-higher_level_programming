i#!/usr/bin/python3
""" This module defines an empty class named square """


class Square:
    """ creating private instance attribute size with conditions """
    def __init__(self, size=0):
        """ initialize a new square """
        self.__size = size

    @property
    def size(self):
        """ Get current size of the square """
        return self.__size

    @size.setter
    def size(self, value):
        """ set current size of the square """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ return the area of the square """
        return self.__size**2

    def my_print(self):
        """ Print the square with the # character. """
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
