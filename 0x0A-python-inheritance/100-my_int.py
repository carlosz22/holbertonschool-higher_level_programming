#!/usr/bin/python3
"""
Module: `100-my_int.py`
"""


class MyInt(int):
    """class MyInt
    Class that inherites from int
    """
    def __eq__(self, other):
        """Compares for inequality"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Compares for equality"""
        return super().__eq__(other)
