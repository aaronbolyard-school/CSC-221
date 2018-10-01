# Aaron Bolyard
# 2018-09-23
# Views Pokemon stored in collections.
# M2HW1, CSC-221, Gold

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

RESULT_ASK_CONTINUE = 1
RESULT_CONTINUE = 2

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

	return RESULT_ASK_CONTINUE

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

	return RESULT_ASK_CONTINUE

def get_filename():
	"""
	Prompts the user for a filename. Returns it.
	"""
	while True:
		value = input("Enter database filename: ").strip()
		if len(value) > 0:
			return value
		else:
			print("Please enter a filename.")

def load_databasemon(database):
	"""
	Loads a Databasemon.

	Prompts the user for the filename. Loads the Databasemon from the file.
	"""
	filename = get_filename()

	try:
		database.load(filename)
		print("Loaded database.")
	except Exception as e:
		print("Couldn't load database from file:")
		print(e)

	return RESULT_CONTINUE

def save_databasemon(database):
	"""
	Saves a Databasemon.

	Prompts the user for the filename. Saves the Databasemon to the file.
	"""
	filename = get_filename()

	try:
		database.save(filename)
		print("Saved database.")
	except Exception as e:
		print("Couldn't save database to file:")
		print(e)

	return RESULT_CONTINUE

def clear_database(database):
	"""
	Clears a database.
	"""
	database.clear()

	print("Cleared database.")


OPERATIONS = {
	'1': list_all_pokemon,
	'2': find_specific_pokemon,
	'C': clear_database,
	'S': save_databasemon,
	'L': load_databasemon,
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
		print("C) Clear database.")
		print("S) Save database.")
		print("L) Load database.")
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

DATABASES = {
	'1': Databasemon.DatabasemonSQL,
	'2': Databasemon.DatabasemonList,
	'3': Databasemon.DatabasemonMap
}

def get_databasemon_type():
	"""
	Gets a databasemon type.
	"""
	database = None
	while database == None:
		print("1) SQL database")
		print("2) List database")
		print("3) Map database")
		value = input("Select an option: ")

		database = DATABASES.get(value.upper(), None)
		if database == None:
			print("Invalid option.")

	return database

def main():
	"""
	Main app loop.
	
	1) Creates the database.
	2) Prompts user for menu option.
	3) Exectues menu operation.
	4) Asks the user to continue.
	"""
	DatabasemonType = get_databasemon_type()
	database = DatabasemonType("pokemon.csv")

	while True:
		print()
		operation = get_operation()

		if operation == False:
			break

		mode = operation(database)
		print()

		if mode == RESULT_ASK_CONTINUE and not should_continue():
			break

	print("Good-bye!")

if __name__ == "__main__":
	main()
