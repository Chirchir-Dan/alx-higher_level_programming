#!/usr/bin/python3
"""
This module provides a class Base
"""


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
        dummy_instance = cls(1, 1)

        # Update dummy instance with real values from dictionary
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances loaded from a JSON file.

        The filename must be <Class name>.json.

        If the file doesn’t exist, return an empty list.
        Otherwise, return a list of instances of the class.

        Returns:
            list: A list of instances loaded from the JSON file.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_data = file.read()
        except FileNotFoundError:
            return []

        data_list = json.loads(json_data)
        instance_list = []
        for data in data_list:
            instance_list.append(cls.create(**data))
        return instance_list
