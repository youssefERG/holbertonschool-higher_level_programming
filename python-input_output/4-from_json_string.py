#!/usr/bin/python3
"""Module that returns a Python object from a JSON string."""
import json


def from_json_string(my_str):
    """Return a Python object represented by a JSON string."""
    return json.loads(my_str)
