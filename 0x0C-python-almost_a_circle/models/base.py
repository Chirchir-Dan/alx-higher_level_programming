#!/usr/bin/python3
"""
This module provides a class Base
"""


import os.path
import json


class Base:
    """
    The is is the base class for this project
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: The JSON string representation of list_dictionaries.
        """

        if not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): A list of instances.

        Returns:
            None
        """
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"

        # Convert instances to dictionaries and then to JSON string
        dict_list = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(dict_list)

        with open(filename, "w", encoding="utf-8") as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of dictionaries represented by the
        JSON string.

        Args:
            json_string (str): A string representing a list of
            dictionaries in JSON format.

        Returns:
            list: A list of dictionaries represented by json_string.
        """
        if not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set using
        **dictionary.

        Args:
            **dictionary: A dictionary containing attribute names
            and their values.

        Returns:
            Base: An instance of the class with attributes set
            according to the dictionary.
        """
        # Create a dummy instance
        if cls.__name__ == "Rectangle":
            from models.rectangle import Rectangle
            dummy_instance = Rectangle(1, 1)
            dummy_instance.update(**dictionary)
            return dummy_instance
        elif cls.__name__ == "Square":
            from models.square import Square
            dummy_instance = Square(1)
            dummy_instance.update(**dictionary)
            return dummy_instance

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serializes a list of objects to a CSV file.

        Args:
            list_objs (list): A list of objects to serialize.

        Returns:
            None
        """
        filename = f"{cls.__name__}.csv"
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    row = [obj.id, obj.width, obj.height, obj.x, obj.y]
                elif cls.__name__ == "Square":
                    row = [obj.id, obj.size, obj.x, obj.y]
                writer.writerow(row)

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserializes objects from a CSV file.

        Returns:
            list: A list of deserialized objects.
        """
        filename = f"{cls.__name__}.csv"
        objects = []
        try:
            with open(filename, 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        obj = Rectangle(*map(int, row))
                    elif cls.__name__ == "Square":
                        obj = Square(*map(int, row))
                    objects.append(obj)
        except FileNotFoundError:
            pass
        return objects
