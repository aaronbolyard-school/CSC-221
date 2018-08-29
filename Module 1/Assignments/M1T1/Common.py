"""
Author: Aaron Bolyard
Common methods.
"""

import math

def get_float(prompt, filter=None):
	"""
	Gets an float from the user after presenting a prompt.

	If a filter is provided, it is expected to return True or False
	depending on if input is valid or invalid.

	Input is validated. A space is automatically appened to the end
	of the prompt.
	"""

	line = input(prompt + " ")
	try:
		value = float(line)

		if filter != None and not filter(value):
			print("Input value not valid; please try again.")
			return get_float(prompt, filter)

		return value
	except ValueError:
		print("Input not an float; please try again.")
		return get_float(prompt, filter)

def calc_min_dimension(length, max_length):
	"""
	Calculates the missing dimension.

	'length' is the length of the object; max_length is the maximum
	length of one side.

	Handles the case where the item length is less than max length.

	Returns the missing dimension.
	"""

	triangle_hypotenuse = max(length, max_length)
	triangle_side = min(length, max_length)

	triangle_hypotenuse_squared = triangle_hypotenuse * triangle_hypotenuse
	triangle_side_squared = triangle_side * triangle_side

	triangle_lengths_difference = triangle_hypotenuse_squared - triangle_side_squared

	other_length = math.sqrt(triangle_lengths_difference)

	return other_length

def calc_diagonal(width, depth):
	"""
	Calculates the diagonal of a box width units by depth units in size.
	"""
	width_squared = width * width
	depth_squared = depth * depth

	width_depth_squared_sum = width_squared + depth_squared

	hypotenuse = math.sqrt(width_depth_squared_sum)

	return hypotenuse
