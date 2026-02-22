#!/usr/bin/python3
"""Module that defines an abstract Animal class and its subclasses."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class representing a generic animal."""

    @abstractmethod
    def sound(self):
        """Return the sound made by the animal."""
        pass


class Dog(Animal):
    """Class representing a dog that implements the Animal interface."""

    def sound(self):
        """Return the sound made by the dog."""
        return "Bark"


class Cat(Animal):
    """Class representing a cat that implements the Animal interface."""

    def sound(self):
        """Return the sound made by the cat."""
        return "Meow"