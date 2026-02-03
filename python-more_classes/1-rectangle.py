#!/usr/bin/python3
"""Module that defines a Rectangle class with width and height validation."""


class Rectangle:
    """Class that defines a rectangle with width and height."""

    def __init__(self, width=0, height=0):
        """Initialize a rectangle with optional width and height."""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height
