#!/usr/bin/python3

"""Function that prints a square with the character #"""

def print_square(size):

    """Function that prints a square with the character #"""

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0: # if size is negative
        raise ValueError("size must be >= 0")
    if size == 0: # if size is 0
        print()
    for i in range(size): # print the square
        for j in range(size):
            print("#", end="")
        print()
