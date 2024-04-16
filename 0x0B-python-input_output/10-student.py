#!/usr/bin/python3
"""Module containing the Student class"""


class Student:
    """
    Defines a student by first_name, last_name, and age.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list): A list of strings containing attribute names.

        Returns:
            dict: A dictionary containing the attributes of the \
                    Student instance.
        """

        if attrs is None:
            return self.__dict__

        student_dict = {}
        for attr in attrs:
            try:
                new_dict[item] = self.__dict__[item]
            except Exception:
                pass
        return student_dict
