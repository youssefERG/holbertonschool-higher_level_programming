#!/usr/bin/python3
"""Module that defines a class Square that inherits from Rectangle."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square, inherits from Rectangle."""

    def __init__(self, size):
        """Initialize a square with size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

    def __str__(self):
        """Return the string representation of the square."""
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
