#!/usr/bin/python3
"""
Module: `1-my_list.py`
"""


class MyList(list):
    """class MyList
    New class that inherits from list
    """

    def print_sorted(self):
        """Print sort list"""
        sorted_list = sorted(self)
        print(sorted_list)
