#!/usr/bin/python3
"""Module that defines mixins and a Dragon class using them."""


class SwimMixin:
    """Mixin that provides swimming capability."""

    def swim(self):
        """Print swimming behavior."""
        print("The creature swims!")


class FlyMixin:
    """Mixin that provides flying capability."""

    def fly(self):
        """Print flying behavior."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Class representing a dragon with swimming and flying abilities."""

    def roar(self):
        """Print roaring behavior of the dragon."""
        print("The dragon roars!")


if __name__ == "__main__":
    draco = Dragon()
    draco.swim()
    draco.fly()
    draco.roar()