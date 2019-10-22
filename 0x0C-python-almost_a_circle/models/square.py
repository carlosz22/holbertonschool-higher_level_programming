#!/usr/bin/python3
"""
Module: square
Creates class Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class Square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, size):
        """size setter"""
        self.width = size
        self.height = size

    def __str__(self):
        """Returns the formal representation of Rectangle"""
        string = "[Square] " \
                 "({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
        return string

    def update(self, *args, **kwargs):
        """Updates the attributes of a Square"""
        attribute_list = ["id", "size", "x", "y"]
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
        attribute_list = ["id", "size", "x", "y"]
        attribute_dict = dict()
        for i in attribute_list:
            attribute_dict[i] = getattr(self, i)
        return attribute_dict
