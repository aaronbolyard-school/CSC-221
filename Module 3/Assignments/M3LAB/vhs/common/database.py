import click
from flask import current_app, g
from flask.cli import with_appcontext

from vhs.model.main import db

from vhs.model.movie import Movie
from vhs.model.rental import Rental
from vhs.model.customer import Customer

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

	movie = Movie(title='Bob',price_code=Movie.PRICE_REGULAR)
	database.session.add(movie)
	database.session.commit()

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
