#!/usr/bin/python3
"""Module that defines Fish, Bird, and FlyingFish classes."""


class Fish:
    """Class representing a fish."""

    def swim(self):
        """Print swimming behavior of a fish."""
        print("The fish is swimming")

    def habitat(self):
        """Print habitat of a fish."""
        print("The fish lives in water")


class Bird:
    """Class representing a bird."""

    def fly(self):
        """Print flying behavior of a bird."""
        print("The bird is flying")

    def habitat(self):
        """Print habitat of a bird."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Class representing a flying fish with multiple inheritance."""

    def fly(self):
        """Print flying behavior of a flying fish."""
        print("The flying fish is soaring!")

    def swim(self):
        """Print swimming behavior of a flying fish."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Print habitat of a flying fish."""
        print("The flying fish lives both in water and the sky!")


if __name__ == "__main__":
    ff = FlyingFish()
    ff.fly()
    ff.swim()
    ff.habitat()
    print(FlyingFish.mro())