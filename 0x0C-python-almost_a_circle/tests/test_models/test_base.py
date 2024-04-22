#!/usr/bin/python3
"""
Unittest for Base class
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseMethods(unittest.TestCase):
    """Test case for Base class"""

    def test_init(self):
        """Test __init__ method"""
        base1 = Base()
        self.assertEqual(base1.id, 1)

    def test_to_json_string(self):
        """Test to_json_string method"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4, 3, 9)
        json_string = Base.to_json_string([r1.to_dictionary(), r2.to_dictionary()])
        expected_string = '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}, {"id": 2, "width": 2, "height": 4, "x": 3, "y": 9}]'
        self.assertEqual(json_string, expected_string)

    def test_from_json_string(self):
        """Test from_json_string method"""
        json_string = '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}, {"x": 3, "width": 2, "id": 2, "height": 4, "y": 9}]'
        dict_list = Base.from_json_string(json_string)
        expected_dict_list = [{'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}, {'x': 3, 'width': 2, 'id': 2, 'height': 4, 'y': 9}]
        self.assertEqual(dict_list, expected_dict_list)

    def test_create_rectangle(self):
        """Test create method for Rectangle"""
        rect_dict = {'id': 1, 'width': 10, 'height': 7, 'x': 2, 'y': 8}
        rect = Rectangle.create(**rect_dict)
        self.assertIsInstance(rect, Rectangle)
        self.assertEqual(rect.id, 1)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 7)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 8)

    def test_create_square(self):
        """Test create method for Square"""
        square_dict = {'id': 2, 'size': 5, 'x': 3, 'y': 9}
        square = Square.create(**square_dict)
        self.assertIsInstance(square, Square)
        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 9)


if __name__ == '__main__':
    unittest.main()

