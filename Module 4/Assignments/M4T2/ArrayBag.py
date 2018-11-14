# Aaron Bolyard
# 2018-10-29
# Array bag implementation.
# M4T2

from Array import Array
from BagInterface import BagInterface

class ArrayBag(BagInterface):
	def __init__(self, sourceCollection = None):
		if sourceCollection:
			self._array = Array(len(sourceCollection))

			index = 0
			for item in sourceCollection:
				self._array[index] = item
				index += 1
		else:
			self._array = Array(0)

	def __str__(self):
		result = '('
		count = len(self)
		index = 0
		for item in self:
			result += str(item)
			index += 1
			if index < count:
				result += ', '
		result += ')'

		return result

	def isEmpty(self):
		return self._array.size() == 0

	def __len__(self):
		return self._array.size()

	def __iter__(self):
		for i in range(self._array.size()):
			yield self._array[i]

	def __add__(self, other):
		result = ArrayBag(self)
		for item in other:
			result.add(item)

		return result

	def __eq__(self, other):
		for item in self:
			if not item in other:
				return False

		for item in other:
			if not item in self:
				return False

		return True

	def __contains__(self, item):
		for i in self:
			if i == item:
				return True

		return False

	def clear(self):
		self._array.shrink(self._array.size())

	def add(self, item):
		self._array.grow(1)
		self._array[self._array.size() - 1] = item

	def remove(self, item):
		foundItem = False

		index = 0
		while index < self._array.size():
			if self._array[index] == item:
				back = self._array.size() - 1

				self._array[back], self._array[index] = self._array[index], self._array[back]
				self._array.shrink(1)

				foundItem = True
			else:
				index += 1

		if not foundItem:
			raise KeyError("item not in bag")
