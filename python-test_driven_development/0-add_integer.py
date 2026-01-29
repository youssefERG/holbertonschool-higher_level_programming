#!/usr/bin/python3
"""Module that adds two integers and returns the result."""


def add_integer(a, b=98):
    """Return the addition of two integers."""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
