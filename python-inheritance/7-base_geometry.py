#!/usr/bin/python3
"""Module that defines a class BaseGeometry."""


class BaseGeometry:
    """Represents base geometry."""

    def area(self):
        """Raise exception because area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name=None, value=None):
        """Validate value as an integer greater than 0."""
        if name is None or value is None:
            raise TypeError("integer_validator() missing arguments")

        if type(value) is not int:
            raise TypeError(name + " must be an integer")

        if value <= 0:
            raise ValueError(name + " must be greater than 0")
