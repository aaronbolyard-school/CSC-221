# Aaron Bolyard
# 2018-09-10
# Allows the user to perform operations on strings.
# M2T1, CSC-221

import Letterology

def print_result(result, type):
	"""
	Prints the results.

	'results' is expected to be a set.
	
	'type' should be a string describing the types of letters in
	'results'.
	"""
	print(str.format("Your string has the following {0}.", type))
	for character in result:
		print("\t", character, sep="")

def do_has_which_vowels():
	"""
	Logic for bronze requirement.
	"""
	value = input("Enter a string: ")

	result = Letterology.has_which_vowels(value)

	print_result(result, "vowels")

def do_has_which_letters():
	"""
	Logic for silver requirement.
	"""
	value = input("Enter which letters to search for: ")
	letters = input("Enter string to search: ")

	result = Letterology.has_which_letters(value, letters)
	print_result(result, "letters")

OPERATIONS = {
	'A': do_has_which_vowels,
	'B': do_has_which_letters
}

def get_operation():
	"""
	Requests the user to provide an option.

	Validates input. Only an existing operation can be requested.

	Returns the operation as a function.
	"""
	operation = None
	while operation == None:
		print("A) Search for vowels in a string")
		print("B) Search for arbitrary letters in a string")
		value = input("Select an option: ")

		operation = OPERATIONS.get(value.upper(), None)
		if not operation:
			print("Invalid option.")

	return operation

def should_continue():
	"""
	Prompts the user to continue.

	Only accepts 'y' and 'n' (case insensitive) as input.

	Returns true if the program should continue, false otherwise.
	"""
	while True:
		option = input("Continue? [Y]es/[N]o: ").lower()

		if option == "y":
			return True
		elif option == "n":
			return False
		else:
			print("Please enter 'y' for yes or 'n' for no.")

def main():
	while True:
		operation = get_operation()

		operation()

		if not should_continue():
			break

if __name__ == "__main__":
	main()
