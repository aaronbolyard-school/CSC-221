# Aaron Bolyard
# 2018-10-29
# Tests updated node methods.
# M3HW, CSC-221

from nodes import Node, length, insert

def test_insert():
	NAMES = [ 'bob', 'sam', 'jane', 'august' ]
	head = insert(0, NAMES[0])
	insert(1, NAMES[2], head)
	insert(1, NAMES[1], head)
	insert(100, NAMES[3], head)

	index = 0
	current = head
	while current != None:
		assert(current.data == NAMES[index])
		index += 1
		current = current.next
	assert(index == 4)

def test_length():
	head = insert(0, 1)
	insert(100, 2, head)
	insert(100, 3, head)
	insert(100, 4, head)

	assert(length(head) == 4)