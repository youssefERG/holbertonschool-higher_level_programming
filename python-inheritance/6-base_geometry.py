#!/usr/bin/python3
"""Module that defines a class BaseGeometry with an area method."""


class BaseGeometry:
    """Represents base geometry."""

    def area(self):
        """Raise an exception indicating area() is not implemented."""
        raise Exception("area() is not implemented")
