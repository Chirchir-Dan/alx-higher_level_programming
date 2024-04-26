#!/usr/bin/python3

import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_square_creation(self):
        # Test Square(1)
        square = Square(1)
        self.assertEqual(square.size, 1)

    def test_square_creation_with_coordinates(self):
        # Test Square(1, 2, 3)
        square = Square(1, 2, 3)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_invalid_size_type(self):
        # Test Square("1")
        with self.assertRaises(TypeError):
            square = Square("1")

    def test_invalid_x_type(self):
        # Test Square(1, "2")
        with self.assertRaises(TypeError):
            square = Square(1, "2")

    def test_invalid_y_type(self):
        # Test Square(1, 2, "3")
        with self.assertRaises(TypeError):
            square = Square(1, 2, "3")

    def test_invalid_size_value(self):
        # Test Square(-1)
        with self.assertRaises(ValueError):
            square = Square(-1)

    def test_invalid_x_value(self):
        # Test Square(1, -2)
        with self.assertRaises(ValueError):
            square = Square(1, -2)

    def test_invalid_y_value(self):
        # Test Square(1, 2, -3)
        with self.assertRaises(ValueError):
            square = Square(1, 2, -3)

    def test_area(self):
        # Test area() method
        square = Square(3)
        self.assertEqual(square.area(), 9)

    def test_str_representation(self):
        # Test __str__() method
        square = Square(3, 4, 5, 6)
        self.assertEqual(str(square), "[Square] (6) 4/5 - 3")

    def test_to_dictionary_method(self):
        # Test to_dictionary() method
        square = Square(3, 4, 5, 6)
        square_dict = {'id': 6, 'size': 3, 'x': 4, 'y': 5}
        self.assertEqual(square.to_dictionary(), square_dict)

    def test_update_method_with_args(self):
        # Test update() method with args
        square = Square(1)
        square.update(89, 2, 3, 4)
        self.assertEqual(str(square), "[Square] (89) 3/4 - 2")

    def test_update_method_with_kwargs(self):
        # Test update() method with kwargs
        square = Square(1)
        square.update(id=89, size=2, x=3, y=4)
        self.assertEqual(str(square), "[Square] (89) 3/4 - 2")

if __name__ == "__main__":
    unittest.main()
