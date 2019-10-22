#!/usr/bin/python3
"""
Module: Rectangle
Creates the class Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Width getter"""
        return self.__width

    @width.setter
    def width(self, width):
        """Width setter"""
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        self.__width = width

    @property
    def height(self):
        """Height getter"""
        return self.__height

    @height.setter
    def height(self, height):
        """Height setter"""
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, x):
        """x setter"""
        if not isinstance(x, int):
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, y):
        """y setter"""
        if not isinstance(y, int):
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y

    def area(self):
        """Returns the area (width * height)"""
        return self.__width * self.__height

    def display(self):
        """Prints the informal representation of Rectangle"""
        print("\n" * self.__y, end='')
        for i in range(self.__height):
            print(" " * self.__x, end='')
            print("#" * self.__width)

    def __str__(self):
        """Returns the formal representation of Rectangle"""
        string = "[Rectangle] ({}) {}/{}" \
                 " - {}/{}".format(self.id, self.__x,
                                   self.__y, self.__width, self.height)
        return string

    def update(self, *args, **kwargs):
        """Updates the attributes of a Rectangle"""
        attribute_list = ["id", "width", "height", "x", "y"]
        if args is not None and len(args) > 0:
            for i in range(len(args)):
                if i >= len(attribute_list):
                    break
                setattr(self, attribute_list[i], args[i])
        else:
            for key, value in kwargs.items():
                if key in attribute_list:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return a dictionary of attributes"""
        attribute_list = ["id", "width", "height", "x", "y"]
        attribute_dict = dict()
        for i in attribute_list:
            attribute_dict[i] = getattr(self, i)
        return attribute_dict
