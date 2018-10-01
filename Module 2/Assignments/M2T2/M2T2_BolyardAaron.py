# Aaron Bolyard
# 2018-10-01
# Stores grade data.
# M2T2, CSC-221

from Grades import Grades

def main():
	grades = Grades()
	grades.load("students.csv")

	print("Students in alphabetical order, by name:")
	for student in grades.byName():
		student.print()
	print()

	print("Students in order of GPA, from low to high:")
	for student in grades.byGPA():
		student.print()
	print()

	print("Good-bye!")

if __name__ == "__main__":
	main()
