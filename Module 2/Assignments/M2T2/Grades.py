# Aaron Bolyard
# 2018-10-01
# Stores grade data.
# M2T2, CSC-221

import csv
import pickle
from Student import Student

class Grades:
	def __init__(self):
		"""
		Constructor. Initializes an empty collection of grades.
		"""
		self.__students = []

	def loadFromCSV(self, filename):
		"""
		Additively loads students from 'filename'.

		The file is expected to be a CSV. Columns, in order:

		- NAME: Name of student (string)
		- PROGRAM: Program of student (string)
		- GPA: GPA of student (float)

		There is expected to be a header.
		"""
		with open(filename, 'r') as file:
			reader = csv.reader(file)
			header = True
			for row in reader:
				if header:
					header = False
					continue

				name = row[0].strip()
				program = row[1].strip()
				try:
					gpa = float(row[2])
				except:
					gpa = 0.0
					print(str.format("Error reading GPA for %s.", name))

				self.__students.append(Student(name, program, gpa))

	def saveToBinary(self, filename):
		"""
		Saves to a binary file.
		"""
		students = []
		for student in self.__students:
			students.append((
				student.getName(),
				student.getProgram(),
				student.getGPA(),
			))

		with open(filename, 'wb') as file:
			pickle.dump(students, file)

	def loadFromBinary(self, filename):
		"""
		Additively loads students from a binary file previously saved by
		saveToBinary.
		"""
		with open(filename, 'rb') as file:
			students = pickle.load(file)
			for student in students:
				self.__students.append(Student(student[0], student[1], student[2]))

	def print(self):
		"""
		Useful method. Iterates over students and prints grades.
		"""
		for student in self.__students:
			student.print()

	def byName(self, reverse=False):
		"""
		Returns a sorted array of students by name (alphabetical order).

		If true, 'reverse' will reverse the order. Amazing!
		"""
		return self.by(lambda s: s.getName().lower(), reverse=reverse)

	def byGPA(self, reverse=False):
		"""
		Returns a sorted array of students by GPA, in ascending order (smallest
		to largest).

		If true, 'reverse' will reverse the order, so highest to lowest. Whodunnit?
		"""
		return self.by(lambda s: s.getGPA(), reverse=reverse)

	def by(self, key, reverse=False):
		"""
		Custom method to sort students.

		'key' is a lambda or function that returns a sortable value.

		If true, 'reverse' reverses the order of the result.
		"""
		students = self.__students[:]
		students.sort(key=key,reverse=reverse)

		return students
