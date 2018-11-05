# Aaron Bolyard
# 2018-10-29
# Tests updated array class.
# M3HW, CSC-221
from arrays import Array

def test_grow():
	items = Array(10, 132)

	items[5] = 0
	items.grow(10)

	items[15] = 0

	assert(items.size() == 20)
	assert(items[5] == 0)
	assert(items[11] == 132)
	assert(items[15] == 0)
	assert(items[19] == 132)

def test_shrink():
	items = Array(10, 132)
	items[0] = 0
	items.shrink(5)

	assert(items.size() == 5)
	assert(items[0] == 0)
	assert(items[4] == 132)

def test_grow_shrink():
	items = Array(10, 0)

	for count in range(items.size()):
		items[count] = count

	items.shrink(5)
	items.grow(5)

	assert(items.size() == 10)
	assert(items[4] == 4)
	assert(items[9] == 0)
