# Aaron Bolyard
# 2018-08-29
# Calculates various attributes of a sphere given a radius.
# M1HW Project 1 CSC-221

import math
import Common

def calculate_diameter(radius):
	"""
	Returns the radius of a sphere with the given radius.
	"""
	return radius * 2

def calculate_circumference(radius):
	"""
	Returns the circumference of a sphere with the given radius.
	"""
	return radius * 2 * math.pi

def calculate_surface_area(radius):
	"""
	Returns the surface area of a sphere with the given radius.
	"""
	return 4.0 * math.pi * (radius ** 2)

def calculate_volume(radius):
	"""
	Returns the volume of a sphere with the given radius.
	"""
	return (4.0 / 3.0) * math.pi * (radius ** 3)

def main():
	radius = Common.get_float("Enter the radius of a sphere:", lambda x: x > 0)

	print(str.format("The diameter of the sphere is {0:.4f}.", calculate_diameter(radius)))
	print(str.format("The circumference of the sphere is {0:.4f}.", calculate_circumference(radius)))
	print(str.format("The surface area of the sphere is {0:.4f}.", calculate_surface_area(radius)))
	print(str.format("The volume of the sphere is {0:.4f}.", calculate_volume(radius)))

if __name__ == "__main__":
	main()
