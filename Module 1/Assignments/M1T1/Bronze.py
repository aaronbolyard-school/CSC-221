# CSC221
# M1T1_Bolyard
# Goal: Bronze

"""
Author: Aaron Bolyard
Solves fishing pole problem.
"""

import Common

def main():
	"""
	Gets the length of the fishing pole and max length of a package on the bus
	as user input.

	Outputs a message telling the user if they can fit the fishing pole
	on the bus, if put in a package diagonally, including the size of the
	box (rounded up to the nearest foot). Otherwise, lets the user know the
	item won't fit.
	"""
	item_length = Common.get_float("Enter the length of the fishing pole, in feet:")
	max_length = Common.get_float("Enter the maximum length allowed, in feet:")

	result = Common.calc_min_dimension(item_length, max_length)
	if result > max_length:
		print("The item cannot fit on the bus, even diagonally.")
	else:
		print(str.format("It fits! Use a box {0:d}' wide and {0:d}' deep.", int(max_length + 0.5), int(result + 0.5)))

if __name__ == '__main__':
	main()
