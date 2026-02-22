#!/usr/bin/python3
"""Module for pickling and unpickling a custom Python object."""

import pickle


class CustomObject:
    """Represents a custom object with name, age, and student status."""

    def __init__(self, name, age, is_student):
        """Initialize a CustomObject with name, age, and is_student attributes."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the attributes of the CustomObject in a readable format."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the current object instance to a file using pickle."""
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize a CustomObject instance from a pickle file."""
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
            return obj
        except Exception:
            return None