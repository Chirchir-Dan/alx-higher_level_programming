#!/usr/bin/python3
"""
Unittest for Rectangle class
"""
import unittest
from models.rectangle import Rectangle


class TestRectangleMethods(unittest.TestCase):
    """Test case for Rectangle class"""

    def setUp(self):
        """Set up method to create a rectangle instance"""
        self.rectangle = Rectangle(3, 4, 0, 0, 1)

    def tearDown(self):
        """Clean up after each test method"""
        del self.rectangle

    def test_init(self):
        """Test __init__ method"""
        self.assertEqual(self.rectangle.width, 3)
        self.assertEqual(self.rectangle.height, 4)
        self.assertEqual(self.rectangle.x, 0)
        self.assertEqual(self.rectangle.y, 0)
        self.assertEqual(self.rectangle.id, 1)

    def test_area(self):
        """Test area method"""
        self.assertEqual(self.rectangle.area(), 12)

    def test_display(self):
        """Test display method"""
        # Capture standard output to check if the display is correct
        import sys
        from io import StringIO
        captured_output = StringIO()
        sys.stdout = captured_output
        self.rectangle.display()
        sys.stdout = sys.__stdout__  # Reset redirect.
        expected_output = "###\n###\n###\n###\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_str(self):
        """Test __str__ method"""
        self.assertEqual(str(self.rectangle), "[Rectangle] (1) 0/0 - 3/4")

    def test_update(self):
        """Test update method"""
        self.rectangle.update(2, 5, 6, 1, 1)
        self.assertEqual(str(self.rectangle), "[Rectangle] (2) 1/1 - 5/6")

    def test_to_dictionary(self):
        """Test to_dictionary method"""
        expected_dict = {'id': 1, 'width': 3, 'height': 4, 'x': 0, 'y': 0}
        self.assertEqual(self.rectangle.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()

