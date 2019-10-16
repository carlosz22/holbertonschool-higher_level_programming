#!/usr/bin/python3
"""
Module: `7-base_geometry.py`
"""


class BaseGeometry():
    """class BaseGeometry
    Class with area and integer validator method
    """
    def area(self):
        """Calculates the area"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validates the integer passed to the function"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
