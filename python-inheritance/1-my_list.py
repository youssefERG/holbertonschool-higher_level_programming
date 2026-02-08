#!/usr/bin/python3
"""Module that defines a MyList class inheriting from list."""


class MyList(list):
    """MyList class that inherits from list."""

    def print_sorted(self):
        """Print the list elements in ascending order."""
        print(sorted(self))
