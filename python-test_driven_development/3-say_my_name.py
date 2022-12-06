#!/usr/bin/python3

'''Function that prints my name'''


def say_my_name(first_name, last_name=""):
    '''Function that prints my name'''
    if type(first_name) is not str:
        # TypeError: isinstance() arg 2 must be a type or tuple of types
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        # TypeError: isinstance() arg 2 must be a type or tuple of types
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
