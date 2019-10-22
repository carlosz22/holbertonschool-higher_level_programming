#!/usr/bin/python3
"""
"""
from models.base import Base

class Rectangle(Base):
    """
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """"""
        return self.__width
    
    @width.setter
    def width(self, width):
        """"""
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        self.__width = width
    
    @property
    def height(self):
        """"""
        return self.__height
    
    @height.setter
    def height(self, height):
        """"""
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height
    
    @property
    def x(self):
        """"""
        return self.__x
    
    @x.setter
    def x(self, x):
        """"""
        if not isinstance(x, int):
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x
    
    @property
    def y(self):
        """"""
        return self.__y
    
    @y.setter
    def y(self, y):
        """"""
        if not isinstance(y, int):
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y

    def area(self):
        """"""
        return self.__width * self.__height
    
    def display(self):
        """"""
        print("\n" * self.__y, end='')
        for i in range(self.__height):
            print(" " * self.__x, end='')
            print("#" * self.__width)

    def __str__(self):
        """"""
        string = "[Rectangle] ({}) {}/{}"\
                  " - {}/{}".format(self.id, self.__x,\
                  self.__y, self.__width, self.height)
        return string

    def update(self, *args, **kwargs):
        """"""
        attribute_list = ["id", "width", "height", "x", "y"]
        if args is not None:
            for i in range(len(args)):
                if i >= len(attribute_list):
                    break
                setattr(self, attribute_list[i], args[i])
        
        if args is None or len(args) == 0:
            for key, value in kwargs.items():
                if key in attribute_list:
                    setattr(self, key, value)

    def to_dictionary(self):
        """"""
        attribute_list = ["id", "width", "height", "x", "y"]
        attribute_dict = dict()
        for i in attribute_list:
            attribute_dict[i] = getattr(self, i)
        return attribute_dict
        





    