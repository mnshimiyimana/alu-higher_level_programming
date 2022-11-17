#!/usr/bin/python3
"""
    define a function 'from_json_string'
    import 'json'
"""

import json


def from_json_string(my_str):
    """
        return object represented by a JSON string
    """

    return json.loads(my_str)
