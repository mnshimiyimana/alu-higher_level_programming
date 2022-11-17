#!/usr/bin/python3
"""
    class 'Student'
"""


class Student:
    """
        define class 'Student'
    """

    def __init__(self, first_name, last_name, age):
        """
            init a new Student
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
            retrieve dictionary representation of a Student instance
        """

        return self.__dict__
