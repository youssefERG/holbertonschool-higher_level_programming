#!/usr/bin/python3
"""
Unittests for the max_integer([..]) function.
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function."""

    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([4, 2, 1, 3]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([5, 1, 2, 3]), 5)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.3, 0.7, 2.3]), 2.3)

    def test_mixed_int_float(self):
        self.assertEqual(max_integer([1, 2.5, 3, 0]), 3)

    def test_negatives(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_duplicates(self):
        self.assertEqual(max_integer([3, 3, 3]), 3)

if __name__ == "__main__":
    unittest.main()
