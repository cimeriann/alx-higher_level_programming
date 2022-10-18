#!/usr/bin/python3
"""
    Defines a rectangle class
"""


class Rectangle:
    """ Represent a rectangle """

    def __init__(self, width=0, height=0):
        """ Initialize a new rectangle
        Args:
            width(int): width of a new rectangle
            Height(int): Height of a new rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ Get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """ Set the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """ Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ returns the area of the rectangle """
        return (self.__width * self.__height)

    def perimeter(self):
        """ returns the perimeter of the rectangle """
        if (self.__height or self.__width) == 0:
            return 0
        else:
            return (2 * self.__width + 2 * self.__height)
