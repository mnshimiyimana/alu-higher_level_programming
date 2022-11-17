#!/usr/bin/python3
"""
    define a function 'append_write'
"""


def append_write(filename="", text=""):
    """
        appends a string to end of text file,
        and return num of characters written
    """

    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
