# CSC221
# M1T1_Bolyard
# Goal: Gold

"""
Author: Aaron Bolyard
Methods to solve the fishing pole problem.
"""

import math

import Common

def print_difference(result_builtin, result_custom):
	result_difference = abs(result_builtin - result_custom)

	print(str.format("The custom square root method returned {0:.4f}; the built-in returned {1:.4f}", result_builtin, result_custom))
	print(str.format("This is a difference of {0:.4f}.", result_difference))

def case_fit():
	"""
	Gets the length of the fishing pole and max length of a package on the bus
	as user input.

	Outputs a message telling the user if they can fit the fishing pole
	on the bus, if put in a package diagonally. Otherwise, lets the user
	know the item won't fit.

	If the item fits, prints the item rounded up to the nearest foot.
	"""
	item_length = Common.get_float("Enter the length of the fishing pole, in feet:")
	max_length = Common.get_float("Enter the maximum length allowed, in feet:")

	result_builtin = Common.calc_min_dimension(item_length, max_length)
	result_custom = Common.calc_min_dimension(item_length, max_length, sqrt=Common.square_root)

	if result_builtin > max_length:
		print("The item cannot fit on the bus, even diagonally.")
	else:
		print(str.format("It fits! You need a box {0:d}' wide and {1:d}' deep.", int(math.ceil(max_length)), int(math.ceil(result_builtin))))

	print_difference(result_builtin, result_custom)

def case_size():
	"""
	Gets the length of the fishing pole and dimensions of a package
	as user input.

	Outputs a message telling the user if they can fit the fishing pole
	in the package. Also outputs the largest straight object that can
	fit in the box.
	"""
	item_length = Common.get_float("Enter the length of the fishing pole, in feet:", lambda x: x > 0)
	item_width = Common.get_float("Enter the width of the box, in feet:", lambda x: x > 0)
	item_depth = Common.get_float("Enter the depth of the box, in feet:", lambda x: x > 0)

	result_builtin = Common.calc_diagonal(item_width, item_depth)
	result_custom = Common.calc_diagonal(item_width, item_depth, sqrt=Common.square_root)

	print(str.format("The largest fishing pole that can fit is {0:.02f}'.", result_builtin))
	if item_length <= result_builtin:
		print("Your fishing pole can fit.")
	else:
		print("Your fishing pole cannot fit.")

	print_difference(result_builtin, result_custom)


def get_integer(prompt):
	"""
	Uses a filter to only get integers.
	"""
	return Common.get_float(prompt, lambda x : math.floor(x) - x == 0)

OPTION_FIT = 1
OPTION_SIZE = 2

def get_option():
	"""
	Gets an option. Returns an OPTION_* value.

	Validates input. Keeps asking the user for a valid value if
	necessary.
	"""
	while True:
		print("1) Find the size of a box to fit a fishing pole.")
		print("2) Check if a fishing pole will fit in a box.")
		option = get_integer("Select an option:")

		if option == OPTION_FIT or option == OPTION_SIZE:
			return option

		print("Please select an option.")

def should_continue():
	while True:
		option = input("Continue? [Y]es/[N]o: ").lower()

		if option == 'y':
			return True
		elif option == 'n':
			return False
		else:
			print("Please enter Y for yes or N for no.")

