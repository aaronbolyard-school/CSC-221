# Aaron Bolyard
# 2018-11-14
# M4T1, Array class

"""
File: Array.py

An Array is a restricted list whose clients can use
only [], len, iter, and str.

To instantiate, use

<variable> = array(<capacity>, <optional fill value>)

The fill value is None by default.
"""

class Array(object):
    """Represents an array."""

    def __init__(self, capacity, fillValue = None):
        """Capacity is the static size of the array.
        fillValue is placed at each position."""
        self._items = list()
        self._minCapacity = capacity
        self._logicalSize = capacity
        self._fillValue = fillValue
        for count in range(capacity):
            self._items.append(fillValue)

    def __len__(self):
        """-> The capacity of the array."""
        return len(self._items)

    def size(self):
        return self._logicalSize

    def __str__(self):
        """-> The string representation of the array."""
        return str(self._items)

    def __iter__(self):
        """Supports iteration over a view of an array."""
        return iter(self._items)

    def __getitem__(self, index):
        """Subscript operator for access at index."""
        if index >= 0 and index < self.size():
            return self._items[index]
        else:
            raise IndexError("index must be greater than or equal to zero and less than the logical size")

    def __setitem__(self, index, newItem):
        """Subscript operator for replacement at index."""
        """Subscript operator for access at index."""
        if index >= 0 and index < self.size():
            self._items[index] = newItem
        else:
            raise IndexError("index must be greater than or equal to zero and less than the logical size")

    def grow(self, amount):
        """
        Grows the array by adding 'amount' elements at the end. The fill
        value passed in the constructor will be assigned to any new cells.

        'amount' must be greater than or equal to zero.

        Does nothing if 'amount' equals 0.
        """
        if amount < 0:
            raise ValueError("Cannot shrink array in grow")

        newLength = self._logicalSize + amount
        if newLength > len(self._items):
            newList = list()
            for index in range(len(self._items)):
                newList.append(self._items[index])

            for offset in range(amount): 
                newList.append(self._fillValue)

            self._items = newList
        else:
            for offset in range(amount):
                self._items[self._logicalSize + offset] = self._fillValue

        self._logicalSize = newLength

    def shrink(self, amount):
        """
        Shrinks the array by removing 'amount' elements.
        """
        if amount < 0:
            raise ValueError("Cannot grow array in shrink")

        newLength = self._logicalSize - amount
        if newLength < 0:
            newLength = 0

        self._logicalSize = newLength