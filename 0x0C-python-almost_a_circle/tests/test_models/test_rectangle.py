#!/usr/bin/python3

# test_Rectangle.py

import io
import sys
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_rectangle_creation(self):
        # Test Rectangle(1, 2)
        rect = Rectangle(1, 2)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)

    def test_rectangle_creation_with_coordinates(self):
        # Test Rectangle(1, 2, 3, 4)
        rect = Rectangle(1, 2, 3, 4)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)

    def test_rectangle_zero_width(self):
        # Test Rectangle with width = 0
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_rectangle_zero_height(self):
        # Test Rectangle with height = 0
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_display_method(self):
        # Test display() method
        rect = Rectangle(3, 2)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        rect.display()
        sys.stdout = sys.__stdout__
        rect_output = "###\n###\n"
        self.assertEqual(captured_output.getvalue(), rect_output)

    def test_invalid_width_type(self):
        # Test Rectangle("1", 2)
        with self.assertRaises(TypeError):
            rect = Rectangle("1", 2)

    def test_invalid_height_type(self):
        # Test Rectangle(1, "2")
        with self.assertRaises(TypeError):
            rect = Rectangle(1, "2")

    def test_invalid_x_type(self):
        # Test Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 2, "3")

    def test_invalid_y_type(self):
        # Test Rectangle(1, 2, 3, "4")
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 2, 3, "4")

    def test_invalid_width_value(self):
        # Test Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            rect = Rectangle(-1, 2)

    def test_invalid_height_value(self):
        # Test Rectangle(1, -2)
        with self.assertRaises(ValueError):
            rect = Rectangle(1, -2)

    def test_invalid_x_value(self):
        # Test Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            rect = Rectangle(1, 2, -3)

    def test_invalid_y_value(self):
        # Test Rectangle(1, 2, 3, -4)
        with self.assertRaises(ValueError):
            rect = Rectangle(1, 2, 3, -4)

    def test_area(self):
        # Test area() method
        rect = Rectangle(3, 4)
        self.assertEqual(rect.area(), 12)

    def test_str_representation(self):
        # Test __str__() method
        rect = Rectangle(3, 4, 5, 6, 7)
        self.assertEqual(str(rect), "[Rectangle] (7) 5/6 - 3/4")

    def test_display_method(self):
        # Test display() method
        rect = Rectangle(3, 2)
        rect_output = "###\n###\n"
        
        captured_output = io.StringIO()
        sys.stdout = captured_output # Redirect stdout to capture output
        rect.display()
        sys.stdout = sys.__stdout__  # Reset redirect
        self.assertEqual(captured_output.getvalue(), rect_output)

    def test_to_dictionary_method(self):
        # Test to_dictionary() method
        rect = Rectangle(3, 4, 5, 6, 7)
        rect_dict = {'id': 7, 'width': 3, 'height': 4, 'x': 5, 'y': 6}
        self.assertEqual(rect.to_dictionary(), rect_dict)

    def test_update_method_with_args(self):
        # Test update() method with args
        rect = Rectangle(1, 1)
        rect.update(89, 2, 3, 4, 5)
        self.assertEqual(str(rect), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_method_with_kwargs(self):
        # Test update() method with kwargs
        rect = Rectangle(1, 1)
        rect.update(id=89, width=2, height=3, x=4, y=5)
        self.assertEqual(str(rect), "[Rectangle] (89) 4/5 - 2/3")

if __name__ == "__main__":
    unittest.main()
