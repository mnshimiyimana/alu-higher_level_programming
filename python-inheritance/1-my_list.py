#!/usr/bin/python3
"""
    defining class 'MyList'
"""


class MyList(list):
    """
        develop the sorted list
    """

    def print_sorted(self):
        """
            prints the sorted list
        """
        print(sorted(self))
