#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_print_max(self):
        self.assertAlmostEqual(max_integer([5, 10, 15, 20, -10]), 20)

    def test_string(self):
        self.assertRaises(TypeError, max_integer, [1, 2, "jiji"])
