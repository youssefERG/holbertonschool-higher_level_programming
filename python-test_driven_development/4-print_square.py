#!/usr/bin/python3
"""
This module defines a function that prints a square using the '#' character.
"""
def print_square(size):
    """
    Prints a square of the given size using '#'.

    Args:
        size (int): The size length of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
