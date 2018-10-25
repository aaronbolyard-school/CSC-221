import os

from flask import Flask
from flask_bootstrap import Bootstrap

def create_app(test_config=None):
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_mapping(
		SECRET_KEY='dev',
		SQLALCHEMY_TRACK_MODIFICATIONS=False,
		SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(app.instance_path, 'www.db')
	)

	if test_config is None:
		app.config.from_pyfile('config.py', silent=True)
	else:
		app.config.from_mapping(test_config)

	try:
		os.makedirs(app.instance_path)
	except OSError:
		pass

	Bootstrap(app)

	import vhs.common.database as database
	database.init_app(app)

	import vhs.views.home as home
	import vhs.views.movies as movies
	import vhs.views.customers as customers
	import vhs.views.rentals as rentals
	app.register_blueprint(home.bp)
	app.register_blueprint(movies.bp)
	app.register_blueprint(customers.bp)
	app.register_blueprint(rentals.bp)

	return app
