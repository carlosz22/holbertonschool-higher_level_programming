#!/usr/bin/python3
"""
Module: `0-rectangle.py`
Implementation of the class Rectangle
"""


class Rectangle:
    """Class Rectangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        for i in range(self.__height):
            string += "#" * self.__width
            if i < (self.__height - 1):
                string += "\n"
        return string

    def __repr__(self):
        class_name = self.__class__.__name__
        return "{}({}, {})".format(class_name, self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
