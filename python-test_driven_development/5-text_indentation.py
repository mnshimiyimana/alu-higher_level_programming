#!/usr/bin/python3
"""Function that prints a text with 2 new lines after each of these character"""


def text_indentation(text):
    """Function that prints a text with 2 new lines after each of these characters: ., ? and :"""
    if type(text) is not str: # if text is not a string
        raise TypeError("text must be a string")
        c = 0
        while c < len(text):
          if text[c] == "." or text[c] == "?" or text[c] == ":":
             print(text[c])
                print()
                c += 1
             else:
                print(text[c], end="")
                c += 1
        if text[c] == "." or text[c] == "?" or text[c] == ":":
            print(text[c])
            print()
        else:
            print(text[c], end="")
        c += 1
    print()

