# CSC221
# M1T1_Bolyard
# Goal: Gold

"""
Author: Aaron Bolyard
Solves fishing pole problem.
"""

import math

import Common

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

	result = Common.calc_min_dimension(item_length, max_length)
	if result > max_length:
		print("The item cannot fit on the bus, even diagonally.")
	else:
		print(str.format("It fits! You need a box {0:d}' wide and {1:d}' deep.", int(math.ceil(max_length)), int(math.ceil(result))))

def case_size():
	"""
	Gets the width and depth of a box and tells the user the largest fishing pole
	they can fit inside.
	"""
	item_width = Common.get_float("Enter the width of the box, in feet:", lambda x: x > 0)
	item_height = Common.get_float("Enter the height of the box, in feet:", lambda x: x > 0)

	result = Common.calc_diagonal(item_width, item_height)

	print(str.format("The largest fishing pole is {0:.02f}'.", result))


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
		print("2) Calculate the size of a fishing pole.")
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


def main():
	"""
	Asks the user for a problem to solve; solves the problem; then asks if
	we should continue.
	"""
	running = True
	while running:
		option = get_option()
		if option == OPTION_FIT:
			case_fit()
		elif option == OPTION_SIZE:
			case_size()
		else:
			assert("I'm melting! Invalid option.")

		running = should_continue()

	print("Good-bye!")

if __name__ == '__main__':
	main()
