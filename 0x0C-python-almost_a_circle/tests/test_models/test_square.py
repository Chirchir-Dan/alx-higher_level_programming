import unittest
from models.square import Square

class TestSquareMethods(unittest.TestCase):
    def test_init(self):
        """Test __init__ method"""
        square1 = Square(5)
        self.assertEqual(square1.id, 1)
        self.assertEqual(square1.size, 5)
        self.assertEqual(square1.width, 5)
        self.assertEqual(square1.height, 5)
        self.assertEqual(square1.x, 0)
        self.assertEqual(square1.y, 0)

        square2 = Square(3, 2, 3, 10)
        self.assertEqual(square2.id, 10)
        self.assertEqual(square2.size, 3)
        self.assertEqual(square2.width, 3)
        self.assertEqual(square2.height, 3)
        self.assertEqual(square2.x, 2)
        self.assertEqual(square2.y, 3)

    def test_str(self):
        """Test __str__ method"""
        square = Square(5, 2, 3, 10)
        self.assertEqual(str(square), "[Square] (10) 2/3 - 5")

    def test_size_property(self):
        """Test size property"""
        square = Square(5)
        self.assertEqual(square.size, 5)

        square.size = 8
        self.assertEqual(square.size, 8)
        self.assertEqual(square.width, 8)
        self.assertEqual(square.height, 8)

    def test_update(self):
        """Test update method"""
        square = Square(5)
        square.update(2, 8, 3, 4, 5)
        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 8)
        self.assertEqual(square.width, 8)
        self.assertEqual(square.height, 8)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 4)

        square.update(x=10, y=12, size=4, id=3)
        self.assertEqual(square.id, 3)
        self.assertEqual(square.size, 4)
        self.assertEqual(square.width, 4)
        self.assertEqual(square.height, 4)
        self.assertEqual(square.x, 10)
        self.assertEqual(square.y, 12)

    def test_to_dictionary(self):
        """Test to_dictionary method"""
        square = Square(5, 2, 3, 10)
        expected_dict = {'id': 10, 'size': 5, 'x': 2, 'y': 3}
        self.assertDictEqual(square.to_dictionary(), expected_dict)

if __name__ == '__main__':
    unittest.main()

