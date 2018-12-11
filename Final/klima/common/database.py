import click
from flask import current_app, g
from flask.cli import with_appcontext

from klima.model.main import db

import klima.model.klimamon
import klima.model.species
import klima.model.user
import klima.model.userWeather

def get_database():
	"""
	Gets the database.

	If the database is not open, connects to the database.
	Expects the database to be stored at the "DATABASE" key.

	Returns the database.
	"""
	if 'database' not in g:
		g.database = db

	return g.database

def flush_database():
	db = get_database()
	db.session.commit()

def close_database(app):
	"""
	Closes the databases, freeing all resources.
	"""
	pass

def initialize_database():
	"""
	Initializes the database from the model.
	"""
	database = get_database()
	database.create_all()

def init_app(app):
	db.init_app(app)

	app.teardown_appcontext(close_database)
	app.cli.add_command(initialize_database_command)

@click.command('initialize-database')
@with_appcontext
def initialize_database_command():
	"""
	Clear the existing data and create new tables.
	"""
	initialize_database()
	click.echo('Initialized the database.')
