# Aaron Bolyard
# 2018-09-23
# Stores Pokemon in an in-memory SQLite database.
# M2HW1, CSC-221

import sqlite3
import csv
import pickle
import os

# Constants. These rows are expected to exist in the CSV loaded by Databasemon.
ROW_ID = 'id'
ROW_IDENTIFIER = 'identifier'
ROW_HEIGHT = 'height'
ROW_WEIGHT = 'weight'

class DatabasemonList:
	"""
	Holds a list of maps to query Pokemon.
	"""

	def __init__(self, filename=None):
		"""
		Constructs the Databasemon from a CSV file.

		Expects there to be at least 'id', 'identifier', 'height', and 'weight'
		rows named as such.
		"""
		self.__mons = []

		if filename != None:
			with open(filename, 'r') as file:
				reader = csv.DictReader(file)

				for row in reader:
					row[ROW_ID] = int(row[ROW_ID])
					row[ROW_WEIGHT] = int(row[ROW_WEIGHT])
					row[ROW_HEIGHT] = int(row[ROW_HEIGHT])
					self.__mons.append(row)

	def fuzzy_find_by_name(self, name):
		"""
		Finds a Pokemon in the database by 'name'.

		'name' can be anywhere in the Pokemon's name. For example 'saur' returns
		all Pokemin in thre Venusaur line, including "venusaur-mega".
		"""
		for mon in self.__mons:
			if mon[ROW_IDENTIFIER].find(name) >= 0:
				yield mon

	def list(self, start=1, limit=151):
		"""
		Lists Pokemon in a range.

		Defaults to generation 1 (RBY) (1 through 151 inclusive).
		"""
		for mon in self.__mons:
			if mon[ROW_ID] > start and mon[ROW_ID] <= start + limit:
				yield mon

	def save(self, filename):
		"""
		Saves the database to a file.
		"""
		with open(filename, 'wb') as file:
			pickle.dump(self.__mons, file)

	def from_file(self, filename):
		"""
		Loads a database from a file.
		"""
		with open(filename, 'rb') as file:
			self.__mons = pickle.load(file)

	def clear(self):
		"""
		Clears a database.
		"""
		self.__mons = []

class DatabasemonMap:
	"""
	Holds a list of maps to query Pokemon.
	"""

	def __init__(self, filename=None):
		"""
		Constructs the Databasemon from a CSV file.

		Expects there to be at least 'id', 'identifier', 'height', and 'weight'
		rows named as such.
		"""
		self.__mons = {}

		if filename != None:
			with open(filename, 'r') as file:
				reader = csv.DictReader(file)

				for row in reader:
					row[ROW_ID] = int(row[ROW_ID])
					row[ROW_WEIGHT] = int(row[ROW_WEIGHT])
					row[ROW_HEIGHT] = int(row[ROW_HEIGHT])
					self.__mons[row[ROW_IDENTIFIER]] = row

	def fuzzy_find_by_name(self, name):
		"""
		Finds a Pokemon in the database by 'name'.

		'name' can be anywhere in the Pokemon's name. For example 'saur' returns
		all Pokemin in thre Venusaur line, including "venusaur-mega".
		"""
		mons = []
		for mon in self.__mons:
			if mon.find(name) >= 0:
				mons.append(self.__mons[mon])
		mons.sort(key=lambda a: a[ROW_ID])
		return mons

	def list(self, start=1, limit=151):
		"""
		Lists Pokemon in a range.

		Defaults to generation 1 (RBY) (1 through 151 inclusive).
		"""
		mons = []
		for mon in self.__mons.values():
			if mon[ROW_ID] > start and mon[ROW_ID] <= start + limit:
				mons.append(mon)
		mons.sort(key=lambda a: a[ROW_ID])
		return mons

	def save(self, filename):
		"""
		Saves the database to a file.
		"""
		with open(filename, 'wb') as file:
			pickle.dump(self.__mons, file)

	def load(self, filename):
		"""
		Loads a database from a file.
		"""
		with open(filename, 'rb') as file:
			self.__mons = pickle.load(file)

	def clear(self):
		"""
		Clears a database.
		"""
		self.__mons = {}

class DatabasemonSQL:
	"""
	Holds a database to query Pokemon.
	"""

	def __init__(self, filename, output=":memory:"):
		"""
		Constructs the Databasemon from a CSV file.

		Expects there to be at least 'id', 'identifier', 'height', and 'weight'
		rows named as such.
		"""

		self.__connection = sqlite3.connect(
			output,
			detect_types=sqlite3.PARSE_DECLTYPES)
		self.__connection.row_factory = sqlite3.Row

		with open('schema.sql', 'rb') as file:
			self.__connection.executescript(file.read().decode('utf-8'))

		if filename != None:
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

	def clear(self):
		"""
		Clears a database.
		"""
		self.__connection.execute(
			"DELETE FROM Mon");
		self.__connection.commit()

	def save(self, filename):
		"""
		Saves a database to a file.
		"""
		try:
			os.remove(filename)
		except:
			# We don't care if the file is actually removed.
			pass

		database = DatabasemonSQL(None, output=filename)

		mons = self.__connection.execute('SELECT * FROM Mon').fetchall()
		for mon in mons:
			database.__connection.execute(
				"INSERT INTO  Mon(id, identifier, weight, height) VALUES(:id, :identifier, :weight, :height)",
				mon)
		database.__connection.commit()

	def load(self, filename):
		"""
		Loads a database from a file.
		"""
		self.__connection = sqlite3.connect(
			filename,
			detect_types=sqlite3.PARSE_DECLTYPES)
