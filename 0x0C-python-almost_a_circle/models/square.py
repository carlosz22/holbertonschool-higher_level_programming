#!/usr/bin/python3
"""
"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """"""
        return self.width

    @size.setter
    def size(self, size):
        """"""
        self.width = size
        self.height = size

    def __str__(self):
        string = "[Square] "\
                  "({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
        return string

    def update(self, *args, **kwargs):
        """"""
        attribute_list = ["id", "size", "x", "y"]
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
        attribute_list = ["id", "size", "x", "y"]
        attribute_dict = dict()
        for i in attribute_list:
            attribute_dict[i] = getattr(self, i)
        return attribute_dict


