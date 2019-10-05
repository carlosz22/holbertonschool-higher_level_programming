#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_print_max(self):
        self.assertEqual(max_integer([5, 10, 15, 20, -10]), 20)

    def test_string_in_list(self):
        self.assertRaises(TypeError, max_integer, [1, 2, "jiji"])

    def test_tuple(self):
        self.assertEqual(max_integer((3, 4, 6, -1, -9, 8)), 8)

    def test_two(self):
        self.assertEqual(max_integer([2, 2, 1, -1]), 2)

    def test_more_than_two(self):
        self.assertEqual(max_integer([1, 2, 5, 3, 5, 5]), 5)

    def test_negative_integer(self):
        self.assertEqual(max_integer([-4, -3, -2]), -2)

    def test_float(self):
        self.assertAlmostEqual(max_integer([3.0, 4.0, -54.0, 23.50]), 23.50)

    def test_same_element(self):
        self.assertEqual(max_integer([10, 10, 10]), 10)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_no_args(self):
        self.assertEqual(max_integer(), None)

    def test_one_element(self):
        self.assertEqual(max_integer([9]), 9)
