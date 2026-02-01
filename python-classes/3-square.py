#!/usr/bin/python3
"""This module defines a Square class with size validation and area."""


class Square:
    """This class represents a square with a validated size."""

    def __init__(self, size=0):
        """Initialize a square and validate the provided size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current square area."""
        return self.__size * self.__size
