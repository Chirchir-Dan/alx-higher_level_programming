#!/usr/bin/python3
"""Module defining the class Student based on 9-student.py"""


class Student:
    """
    Class that defines properties of student.

    Attributes:
        first_name (str): first name of student.
        last_name (str): last name of student.
        age (int): age of student.
    """
    def __init__(self, first_name, last_name, age):
        """Creates new instances of Student.

        Args:
            first_name (str): first name of student.
            last_name (str): last name of student.
            age (int): age of student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance.

        If attrs is a list of strings, only attribute names contained in,
        this list must be retrieved.
        Otherwise, all attributes must be retrieved.

        Args:
            attrs (list): A list of strings containing attribute names.

        Returns:
            dict: A dictionary containing the attributes of the Student instance.
        """
        if attrs is None:
            return self.__dict__
        
        student_dict = {}
        for attr in attrs:
            if attr in self.__dict__:
                student_dict[attr] = getattr(self, attr)
        return student_dict
