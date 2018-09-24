import Databasemon

GENERATIONS = [
	('rby',   0, 151),
	('gsc', 151, 100),
	('rse', 251, 135),
	('dpp', 386, 107),
	('bw',  493, 156),
	('sm',  649, 158)
]

def get_integer(prompt, min_value, max_value):
	"""
	Gets an integer between min_value and max_value.

	Prompts the user with prompt, handling proper formatting. Informs the user
	when invalid input is entered and tries again.

	Returns an integer between min_value and max_value.
	"""
	while True:
		try:
			value = input(prompt + " ")
			value_as_integer = int(value)

			if value_as_integer < min_value or value_as_integer > max_value:
				print("Please enter a value within the specified range.")
			else:
				return value_as_integer
		except e as ValueError:
			print("Please enter a valid integer.")
		except:
			print("There's a ghost in the machine...")

def get_generation():
	"""
	Prompts the user to select a generation of Pokemon games.

	Returns the start & count of the Pokemon in Databasemon for that generation.

	Handles invalid input. Only returns when a valid option is selected.
	"""

	generation = None
	while generation == None:
		index = 1
		print("Generations:")
		for generation in GENERATIONS:
			print(str.format("  {0:d}. {1}", index, generation[0]))
			index = index + 1

		selection = get_integer("Select a generation:", 1, len(GENERATIONS))
		selected_generation = GENERATIONS[selection - 1]

		return (selected_generation[1], selected_generation[2])

def list_all_pokemon(database):
	"""
	Lists all Pokemon in a generation.
	"""
	start, count = get_generation()

	first = True
	for mon in database.list(start, count):
		if not first:
			print(', ', end='')
		else:
			first = False

		print(mon['identifier'], end='')
	print()

def find_specific_pokemon(database):
	"""
	Finds a Pokemon using a fuzzy search. The term can be found anywhere in
	the name.

	Returns info about the Pokemon found, such as its Pokedex number, name,
	weight, and height.
	"""

	name = input("Enter a name: ")
	for mon in database.fuzzy_find_by_name(name):
		print(
			str.format("{0}", mon['id']).rjust(5),
			str.format("{0:20s}", mon['identifier']).rjust(20)[:20],
			"Height:", str.format("{0:.1f}m", mon['height'] / 10).rjust(8),
			"Weight:", str.format("{0:.1f}kg", mon['weight'] / 10).rjust(8))


OPERATIONS = {
	'1': list_all_pokemon,
	'2': find_specific_pokemon,
	'Q': False
}

def get_operation():
	"""
	Requests the user to provide an option.

	Validates input. Only an existing operation can be requested.

	Returns the operation as a function.
	"""
	operation = None
	while operation == None:
		print("1) List Pokemon from a generation")
		print("2) Search for Pokemon by name")
		print("Q) Quit")
		value = input("Select an option: ")

		operation = OPERATIONS.get(value.upper(), None)
		if operation == None:
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
	"""
	Main app loop.

	1) Prompts user for menu option.
	2) Exectues menu operation.
	3) Asks the user to continue.
	"""
	database = Databasemon.DatabasemonList("pokemon.csv")

	while True:
		operation = get_operation()

		if operation == False:
			break

		operation(database)

		if not should_continue():
			break

	print("Good-bye!")

if __name__ == "__main__":
	main()
