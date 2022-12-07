#!/usr/bin/python3
"""Class to avoid duplication documentation"""

class Base:
    """Base class documentation"""

nb_objects = 0

    def __init__(self, id=None):
        # Base class constructor
        self.id = id
        if id is not None:
            self.id = id
        else:
            # increment the number of objects
            Base.nb_objects += 1
            self.id = Base.nb_objects
