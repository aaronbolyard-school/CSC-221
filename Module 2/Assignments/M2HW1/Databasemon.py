# Aaron Bolyard
# 2018-09-23
# Stores Pokemon in an in-memory SQLite database.
# M2HW1, CSC-221

import sqlite3
import csv

# Constants. These rows are expected to exist in the CSV loaded by Databasemon.
ROW_ID = 'id'
ROW_IDENTIFIER = 'identifier'
ROW_HEIGHT = 'height'
ROW_WEIGHT = 'weight'

class Databasemon:
	"""
	Holds a database to query Pokemon.
	"""

	def __init__(self, filename):
		"""
		Constructs the Databasemon from a CSV file.

		Expects there to be at least 'id', 'identifier', 'height', and 'weight'
		rows named as such.
		"""
		self.__connection = sqlite3.connect(
			":memory:",
			detect_types=sqlite3.PARSE_DECLTYPES)
		self.__connection.row_factory = sqlite3.Row

		with open('schema.sql', 'rb') as file:
			self.__connection.executescript(file.read().decode('utf-8'))

		with open(filename, 'r') as file:
			reader = csv.DictReader(file)

			for row in reader:
				self.__connection.execute(
					'INSERT INTO Mon(id, identifier, height, weight) VALUES(?, ?, ?, ?)',
					(row[ROW_ID], row[ROW_IDENTIFIER], row[ROW_HEIGHT], row[ROW_WEIGHT]))
			self.__connection.commit()

	def fuzzy_find_by_name(self, name):
		"""
		Finds a Pokemon in the database by 'name'.

		'name' can be anywhere in the Pokemon's name. For example 'saur' returns
		all Pokemin in thre Venusaur line, including "venusaur-mega".
		"""
		return self.__connection.execute(
			'SELECT * FROM Mon WHERE identifier LIKE ?',
			(str.format("%{0}%", name),)).fetchall()

	def list(self, start=1, limit=151):
		"""
		Lists Pokemon in a range.

		Defaults to generation 1 (RBY) (1 through 151 inclusive).
		"""
		return self.__connection.execute(
			'SELECT * FROM Mon LIMIT ? OFFSET ?',
			(limit, start)).fetchall()
