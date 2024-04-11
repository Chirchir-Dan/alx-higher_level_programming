#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Unit test class for testing the max_integer function.
    """

    def test_max_integer_normal_list(self):
        """Test with a normal list of integers."""
        result = max_integer([1, 2, 3, 4, 5])
        self.assertEqual(result, 5)

    def test_max_integer_negative_numbers(self):
        """Test with a list of negative numbers."""
        result = max_integer([-1, -2, -3, -4, -5])
        self.assertEqual(result, -1)

    def test_max_integer_empty_list(self):
        """Test with an empty list."""
        result = max_integer([])
        self.assertIsNone(result)

    def test_max_integer_single_element(self):
        """Test with a list containing a single element."""
        result = max_integer([7])
        self.assertEqual(result, 7)

    def test_max_integer_duplicate_max(self):
        """Test with a list containing duplicate maximum values."""
        result = max_integer([5, 5, 5, 5])
        self.assertEqual(result, 5)

    def test_max_integer_float_numbers(self):
        """Test with a list of floating-point numbers."""
        result = max_integer([3.5, 2.9, 7.1, 4.8])
        self.assertEqual(result, 7.1)

    def test_max_integer_mixed_list(self):
        """Test with a list containing both integers and floats."""
        result = max_integer([1, 2.5, 3, 4.7, 5])
        self.assertEqual(result, 5)

    def test_max_integer_large_list(self):
        """Test with a large list of integers."""
        result = max_integer(list(range(10000)))
        self.assertEqual(result, 9999)

    def test_max_integer_strings(self):
        """Test with a list of strings."""
        result = max_integer(["apple", "banana", "orange"])
        self.assertIsNone(result)

    def test_max_integer_none(self):
        """Test with None as input."""
        result = max_integer(None)
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
