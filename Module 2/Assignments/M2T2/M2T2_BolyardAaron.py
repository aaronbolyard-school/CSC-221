# Aaron Bolyard
# 2018-10-01
# Stores grade data.
# M2T2, CSC-221

from Grades import Grades
from Student import Student

class Application:
	"""
	Holds application state.
	"""

	def __init__(self):
		self.__grades = None

	def getGrades(self):
		return self.__grades

	def setGrades(self, value):
		self.__grades = value

def do_load_csv(application):
	"""
	Loads grades from a CSV.

	Asks the user for the filename of the CSV. Does nothing in the event of an
	error. Prints said error.
	"""

	grades = Grades()

	filename = input("Enter the filename: ")
	try:
		grades.loadFromCSV(filename)
		application.setGrades(grades)
	except Exception as e:
		print("Failed to load grades:", e)

def do_create_pickle(application):
	"""
	Saves grades to a binary file.

	Asks the user for the filename of the file. Does nothing in the event of an
	error. Prints said error.
	"""

	filename = input("Enter the filename: ")
	try:
		application.getGrades().saveToBinary(filename)
	except Exception as e:
		print("Failed to save grades:", e)

def do_load_pickle(application):
	"""
	Loads the grades from a binary file.

	Asks the user for the filename of the file. Does nothing in the event of an
	error. Prints said error.
	"""

	grades = Grades()

	filename = input("Enter the filename: ")
	try:
		grades.loadFromBinary(filename)
		application.setGrades(grades)
	except Exception as e:
		print("Failed to load grades:", e)

def do_show_by_name(application):
	"""
	Shows grades sorted by name, ascending.
	"""

	if application.getGrades() == None:
		print("Please load a students file.")
	else:
		Student.printHeader()
		for student in application.getGrades().byName():
			student.print()

def do_show_by_gpa(application):
	"""
	Shows grades sorted by GPA, from lowest to highest.
	"""

	if application.getGrades() == None:
		print("Please load a students file.")
	else:
		Student.printHeader()
		for student in application.getGrades().byGPA():
			student.print()

OPERATIONS = {
	'1': do_load_csv,
	'2': do_create_pickle,
	'3': do_load_pickle,
	'4': do_show_by_name,
	'5': do_show_by_gpa,
	'6': False
}

def get_operation():
	"""
	Requests the user to provide an option.

	Validates input. Only an existing operation can be requested.

	Returns the operation as a function.
	"""
	operation = None
	while operation == None:
		print("1. Load CSV")
		print("2. Create pickle file")
		print("3. Load pickle file")
		print("4. Show students by name")
		print("5. Show students by GPA")
		print("6. Quit")
		value = input("Select an option: ")

		operation = OPERATIONS.get(value.upper(), None)
		if operation == None:
			print("Invalid option.")

	return operation

def main():
	application = Application()

	while True:
		operation = get_operation()

		if operation == False:
			break

		print()
		operation(application)
		print()

	print("Good-bye!")

if __name__ == "__main__":
	main()
