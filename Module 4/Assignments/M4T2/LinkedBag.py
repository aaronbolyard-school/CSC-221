# Aaron Bolyard
# 2018-10-29
# Link bag implementation.
# M4T2

import LinkedList
from BagInterface import BagInterface

class LinkedBag(BagInterface):
	def __init__(self, sourceCollection = None):
		self._head = None

		if sourceCollection:
			for item in sourceCollection:
				result = LinkedList.insert(0, item, self._head)
				if not self._head:
					self._head = result

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
		return LinkedList.length(self._head) == 0

	def __len__(self):
		return LinkedList.length(self._head)

	def __iter__(self):
		current = self._head
		while current != None:
			yield current.data
			current = current.next

	def __add__(self, other):
		result = LinkedBag(self)
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
		self._head = None

	def add(self, item):
		result = LinkedList.insert(0, item, self._head)
		if not self._head:
			self._head = result

	def remove(self, item):
		foundItem = False

		current = self._head
		previous = None
		while current != None:
			if current.data == item:
				if previous:
					previous.next = current.next
				if self._head == current:
					self._head = current.next
				foundItem = True
			previous = current
			current = current.next

		if not foundItem:
			raise KeyError("item not in bag")
