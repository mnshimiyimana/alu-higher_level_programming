#!/usr/bin/python3
"""Function that prints a text with 2 new lines after each of these characters: ., ? and :"""


def text_indentation(text):
    """Function that prints a text with 2 new lines after each of these characters: ., ? and :"""
    if type(text) is not str: # if text is not a string
        raise TypeError("text must be a string")
    for i in range(len(text)):  # for each character in text
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            print(text[i])
            print()
        else: # if the character is not ., ? or :
            print(text[i], end="")
