#!/usr/bin/python3
"""
This module defines a function that prints text with 2 new lines after
each '.', '?', or ':' character.
"""
def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', or ':'.

    Args:
        text (str): The text to be printed.

    Raises:
        TypeError: If text is not a string.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    i = 0
    n = len(text)
    while i < n:
        line = ""
        while i < n and text[i] not in ".?:":
            line += text[i]
            i += 1
        line = line.strip()
        if line:
            print(line, end='')
        if i < n:
            print(text[i], end="\n\n")
            i += 1
