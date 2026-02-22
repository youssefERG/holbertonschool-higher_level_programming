#!/usr/bin/python3
"""Module that defines a VerboseList class extending the built-in list."""


class VerboseList(list):
    """List subclass that prints notifications on modifications."""

    def append(self, item):
        """Append an item to the list and print a notification."""
        super().append(item)
        print("Added {} to the list.".format(item))

    def extend(self, iterable):
        """Extend the list and print a notification."""
        count = len(iterable)
        super().extend(iterable)
        print("Extended the list with {} items.".format(count))

    def remove(self, item):
        """Remove an item from the list and print a notification."""
        print("Removed {} from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Pop an item from the list and print a notification."""
        item = self[index]
        print("Popped {} from the list.".format(item))
        return super().pop(index)


if __name__ == "__main__":
    v = VerboseList([1, 2, 3])
    v.append(4)
    v.extend([5, 6])
    v.remove(2)
    v.pop()
