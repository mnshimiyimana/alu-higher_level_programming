#!/usr/bin/python3
"""
    define a function 'load_from_json_file'
    import 'json'
"""

import json


def load_from_json_file(filename):
    """
        create an object from a JSON file
    """

    with open(filename, encoding='utf-8') as f:
        return json.load(f)
