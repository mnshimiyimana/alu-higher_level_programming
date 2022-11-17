#!/usr/bin/python3
"""
    define a function 'class_to_json'
"""


def class_to_json(obj):
    """
        return dictionary description for JSON object
    """

    return obj.__dict__
