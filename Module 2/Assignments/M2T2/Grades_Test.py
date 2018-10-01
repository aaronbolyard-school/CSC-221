from Grades import Grades

def test_by_name():
	grades = Grades()
	grades.load("students.csv")

	names = grades.byName()

	assert(names[0].getName() == "Alice")
	assert(names[1].getName() == "Bob")
	assert(names[2].getName() == "Charles")
	assert(names[3].getName() == "David")
	assert(names[4].getName() == "Ellen")
	assert(names[5].getName() == "Francine")

def test_by_name_reverse():
	grades = Grades()
	grades.load("students.csv")

	names = grades.byName(reverse=True)

	assert(names[5].getName() == "Alice")
	assert(names[4].getName() == "Bob")
	assert(names[3].getName() == "Charles")
	assert(names[2].getName() == "David")
	assert(names[1].getName() == "Ellen")
	assert(names[0].getName() == "Francine")

def test_by_gpa():
	grades = Grades()
	grades.load("students.csv")

	names = grades.byGPA()

	assert(names[5].getName() == "Francine")
	assert(names[4].getName() == "Alice")
	assert(names[3].getName() == "Charles")
	assert(names[2].getName() == "David")
	assert(names[1].getName() == "Bob")
	assert(names[0].getName() == "Ellen")

def test_by_gpa_reverse():
	grades = Grades()
	grades.load("students.csv")

	names = grades.byGPA(reverse=True)

	assert(names[0].getName() == "Francine")
	assert(names[1].getName() == "Alice")
	assert(names[2].getName() == "Charles")
	assert(names[3].getName() == "David")
	assert(names[4].getName() == "Bob")
	assert(names[5].getName() == "Ellen")
