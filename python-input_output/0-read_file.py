#!/usr/bin/python3
"""Module that reads a UTF-8 text file and prints it to stdout."""


def read_file(filename=""):
    """Read a UTF-8 text file and print its content to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
