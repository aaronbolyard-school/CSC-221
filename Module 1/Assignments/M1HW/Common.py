"""
Author: Aaron Bolyard
Common methods.
"""

import math

def get_float(prompt, filter=None):
	"""
	Gets a float from the user after presenting a prompt.

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
		print("Input not a float; please try again.")
		return get_float(prompt, filter)