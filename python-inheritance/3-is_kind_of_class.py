#!/usr/bin/python3
"""
    defines a function 'is_kind_of_class'
"""


def is_kind_of_class(obj, a_class):
    """
        check if an object is an instance or inherited instance of a class
        Return: - True
                - False
    """
    if isinstance(obj, a_class):
        return True
    return False
