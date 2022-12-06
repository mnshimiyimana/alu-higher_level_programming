#!/usr/bin/python3

"""Function that prints my name"""


if not isinstance(first_name, str):

def say_my_name(first_name, last_name=""):
    """Function that prints my name"""
    # if not isinstance(first_name, str): # TypeError: isinstance() arg 2 must be a type or tuple of types
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
         # TypeError: isinstance() arg 2 must be a type or tuple of types
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
