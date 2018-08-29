# CSC221
# M1T1_Bolyard
# Goal: Gold

"""
Author: Aaron Bolyard
Logic to solve Gold.
"""

from FishingPole import (
	get_option,
	case_fit,
	case_size,
	should_continue,
	OPTION_FIT,
	OPTION_SIZE)

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
