#!/usr/bin/python3

# test_base.py

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_auto_id_assignment(self):
        # Test Base() for automatically assigning an ID
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_auto_id_increment(self):
        # Test Base() for automatically assigning an ID + 1 of the previous one
        obj1 = Base(10)
        obj2 = Base()
        self.assertEqual(obj1.id, 10)
        self.assertEqual(obj2.id, 3)

    def test_id_passed(self):
        # Test Base(89) for saving the passed ID
        obj = Base(89)
        self.assertEqual(obj.id, 89)

    def test_to_json_string_none(self):
        # Test Base.to_json_string(None)
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty_list(self):
        # Test Base.to_json_string([])
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_with_data(self):
        # Test Base.to_json_string([{ 'id': 12 }])
        data = [{'id': 12}]
        self.assertEqual(Base.to_json_string(data), '[{"id": 12}]')

    def test_to_json_string_returns_string(self):
        # Test Base.to_json_string([{ 'id': 12 }]) returns a string
        data = [{'id': 12}]
        json_str = Base.to_json_string(data)
        self.assertIsInstance(json_str, str)

    def test_from_json_string_none(self):
        # Test Base.from_json_string(None)
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty_string(self):
        # Test Base.from_json_string("[]")
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_with_data(self):
        # Test Base.from_json_string('[{ "id": 89 }]')
        data = '[{ "id": 89 }]'
        self.assertEqual(Base.from_json_string(data), [{'id': 89}])

    def test_from_json_string_returns_list(self):
        # Test Base.from_json_string('[{ "id": 89 }]') returns a list
        data = '[{ "id": 89 }]'
        result = Base.from_json_string(data)
        self.assertIsInstance(result, list)

if __name__ == "__main__":
    unittest.main()
