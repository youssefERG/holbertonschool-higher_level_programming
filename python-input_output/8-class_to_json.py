#!/usr/bin/python3
"""Module that returns the dictionary description for JSON serialization."""


def class_to_json(obj):
    """Return the dictionary description of an object for JSON serialization."""
    return obj.__dict__
