# Aaron Bolyard
# 2018-08-30
# Simulates a bouncy ball.
# M1HW Project 3 CSC-221

import math
import Common

# The magical bouncy value of the ball.
# It's like the speed of light, except smaller.
BOUNCE_CONSTANT = 0.6

def main():
	initial_height = Common.get_float("Enter the height of the ball, in feet:")
	num_bounces = Common.get_float("Enter how many times the ball bounces:", lambda x: x > 0 and (math.floor(x) - x) == 0)

	total_distance = 0
	current_bounce = initial_height
	for i in range(int(num_bounces)):
		# The ball drops, then the ball bounces. Simulate both per step.
		total_distance += current_bounce
		current_bounce *= BOUNCE_CONSTANT
		total_distance += current_bounce

	print(str.format("The ball bounced {0:.2f}' in total.", total_distance))

if __name__ == "__main__":
	main()
