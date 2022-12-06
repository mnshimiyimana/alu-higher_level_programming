#!/usr/bin/python3
"""Writing an unittests for the function"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Testing max_integer method"""
    def test_simple_case(self):
        """Testing max_integer method"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative_case(self):
        """Testing max_integer method"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_empty_case(self):
        """Testing max_integer method"""
        self.assertEqual(max_integer([]), None)

    def test_one_element_case(self):
        """Testing max_integer method"""
        self.assertEqual(max_integer([1]), 1)

    def test_string_case(self):
        """Testing max_integer method"""
        self.assertEqual(max_integer("string"), 't')

