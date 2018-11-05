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

	database.session.add(Movie(title='Avengers: Infinity War',price_code=Movie.PRICE_NEW))
	database.session.add(Movie(title='Avengers: Age of Ultron',price_code=Movie.PRICE_REGULAR))
	database.session.add(Movie(title='Avengers',price_code=Movie.PRICE_REGULAR))
	database.session.add(Movie(title='Captain America',price_code=Movie.PRICE_REGULAR))
	database.session.add(Movie(title='Captain America: Winter Soldier',price_code=Movie.PRICE_REGULAR))
	database.session.add(Movie(title='Captain America: Civil War',price_code=Movie.PRICE_REGULAR))
	database.session.add(Movie(title='Iron Man',price_code=Movie.PRICE_REGULAR))
	database.session.add(Movie(title='Iron Man 2',price_code=Movie.PRICE_REGULAR))
	database.session.add(Movie(title='Iron Man 3',price_code=Movie.PRICE_REGULAR))
	database.session.add(Movie(title='Thor',price_code=Movie.PRICE_REGULAR))
	database.session.add(Movie(title='Thor: Dark World',price_code=Movie.PRICE_REGULAR))
	database.session.add(Movie(title='Thor: Ragnorok',price_code=Movie.PRICE_NEW))
	database.session.add(Movie(title='Black Panther',price_code=Movie.PRICE_NEW))
	database.session.add(Movie(title='Ant-Man vs the Wasp',price_code=Movie.PRICE_NEW))
	database.session.add(Movie(title='LEGO Marvel: Avengers',price_code=Movie.PRICE_CHILDREN))
	database.session.add(Movie(title='LEGO Batman',price_code=Movie.PRICE_CHILDREN))
	database.session.add(User(name='Aaron Bolyard'))
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
