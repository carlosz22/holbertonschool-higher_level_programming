#!/usr/bin/python3
"""
Module: `12-student.py`
"""


class Student:
    """class Student
    """
    def __init__(self, first_name, last_name, age):
        """Constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Prints the dictionary representation of the object"""
        normal_dict_flag = False
        if isinstance(attrs, list):
            for element in attrs:
                if not isinstance(element, str):
                    normal_dict_flag = True
        else:
            normal_dict_flag = True

        if normal_dict_flag:
            return self.__dict__

        customized_dict = dict()

        for element in attrs:
            if element in self.__dict__:
                customized_dict[element] = self.__dict__[element]

        return customized_dict
