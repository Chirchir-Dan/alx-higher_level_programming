#!/usr/bin/python3

import os
import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_square_creation(self):
        # Test Square(1)
        square = Square(1)
        self.assertEqual(square.size, 1)

    def test_square_zero_size(self):
        # Test Square with size = 0
        with self.assertRaises(ValueError):
            Square(0)

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

    def test_load_from_file_exists(self):
        # Test load_from_file() when file exists
        filename = "Square.json"
        with open(filename, "w") as file:
            file.write("[{\"id\": 1, \"size\": 2}]")

        squares = Square.load_from_file()
        self.assertEqual(len(squares), 1)
        self.assertEqual(squares[0].id, 1)
        self.assertEqual(squares[0].size, 2)

        os.remove(filename)

    def test_load_from_file_not_exists(self):
        # Test load_from_file() when file doesn't exist
        filename = "Square.json"
        if os.path.exists(filename):
            os.remove(filename)

        squares = Square.load_from_file()
        self.assertEqual(len(squares), 0)

    def test_save_to_file_with_objects(self):
        # Test save_to_file() with a list of objects
        squares = [Square(1)]
        Square.save_to_file(squares)

        filename = "Square.json"
        self.assertTrue(os.path.exists(filename))

        with open(filename, "r") as file:
            data = file.read()
            self.assertNotEqual(data, "[]")

        os.remove(filename)

    def test_save_to_file_empty_list(self):
        # Test save_to_file() with an empty list
        squares = []
        Square.save_to_file(squares)

        filename = "Square.json"
        self.assertTrue(os.path.exists(filename))

        with open(filename, "r") as file:
            data = file.read()
            self.assertEqual(data, "[]")

        os.remove(filename)

    def test_save_to_file_with_none(self):
        # Test save_to_file() with None
        Square.save_to_file(None)

        filename = "Square.json"
        self.assertTrue(os.path.exists(filename))

        with open(filename, "r") as file:
            data = file.read()
            self.assertEqual(data, "[]")

        os.remove(filename)

    def test_create_method_with_all_attributes(self):
        # Test create() method with all attributes
        square = Square.create(id=89, size=1, x=2, y=3)
        self.assertEqual(square.id, 89)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_create_method_without_y_attribute(self):
        # Test create() method without y attribute
        square = Square.create(id=89, size=1, x=2)
        self.assertEqual(square.id, 89)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 0)

    def test_create_method_without_x_and_y_attributes(self):
        # Test create() method without x and y attributes
        square = Square.create(id=89, size=1)
        self.assertEqual(square.id, 89)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)

if __name__ == "__main__":
    unittest.main()
