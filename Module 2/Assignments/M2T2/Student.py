# Aaron Bolyard
# 2018-10-01
# Stores student data.
# M2T2, CSC-221

class Student:
	"""
	An immutable structure representing a student.
	"""
	def __init__(self, name, program, gpa):
		"""
		Creates a student with the given name, program, and GPA.
		"""
		self.__name = name
		self.__program = program
		self.__gpa = gpa

	def getName(self):
		"""
		Returns the name of the student.
		"""
		return self.__name

	def getProgram(self):
		"""
		Returns the program of the student.
		"""
		return self.__program

	def getGPA(self):
		"""
		Returns the GPA of the student.
		"""
		return self.__gpa

	def print(self):
		"""
		Utility method. Nicely prints student information.
		"""
		print(
			self.__name[:20].rjust(20),
			self.__program[:20].rjust(20),
			format(self.__gpa, '.2f').rjust(6))
