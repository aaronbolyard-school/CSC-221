# Aaron Bolyard
# 2018-10-29
# Updated node methods.
#  * Added length method.
#  * Added insert method.
# M3HW, CSC-221

class Node(object):
	def __init__(self, data, next = None):
		"""
		Instantiates a Node with default next of None.
		"""
		self.data = data
		self.next = next

def length(head):
	"""
	Counts the length of the linked provided link list.
	"""

	result = 0
	current = head

	while current != None:
		result += 1
		current = current.next

	return result

def get(head, index):
	"""
	Gets a node at 'index'.

	Returns the last node if 'index' exceeds the length of the list.
	"""

	currentIndex = 0
	previous = None
	current = head

	while currentIndex < index and current != None:
		previous = current
		current = current.next
		currentIndex += 1

	# Return the last node if the index exceeds the length
	# of the linked list.
	if current == None:
		return previous

	return current

def insert(index, data, head=None):
	"""
	Inserts a node at the specified position.

	If the position exceeds the length of the list, it is inserted at
	the end.

	If the list is None, then a new list is created.
	"""
	node = get(head, index - 1)

	if node:
		 	print('node', index, node.data)

	nextNode = None
	if node:
		nextNode = node.next

	result = Node(data, nextNode)

	if node:
		node.next = result

	return result
