# Aaron Bolyard
# 2018-08-30
# Computes pi.
# M1HW Project 4 CSC-221

import math
import Common

# The magical bouncy value of the ball.
# It's like the speed of light, except smaller.
BOUNCE_CONSTANT = 0.6

def main():
	print("This program computes pi.")
	num_iterations = Common.get_float("Enter how many times to iterate:", lambda x: x > 0 and (math.floor(x) - x) == 0)

	current_pi = 1
	current_denominator = 3
	for i in range(int(num_iterations)):
		current_pi -= 1.0 / current_denominator
		current_denominator += 2
		current_pi += 1.0 / current_denominator
		current_denominator += 2
	current_pi *= 4

	print(str.format("PI: {0}.", current_pi))

if __name__ == "__main__":
	main()
