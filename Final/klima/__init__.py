import os

from flask import Flask
from flask_session import Session

def create_app(test_config=None):
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_mapping(
		SECRET_KEY='dev',
		SESSION_TYPE='filesystem',
		SQLALCHEMY_TRACK_MODIFICATIONS=False,
		SQLALCHEMY_COMMIT_ON_TEARDOWN=True,
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

	app.config.from_pyfile("settings.cfg")

	from klima.common.auth import current_user
	app.jinja_env.globals.update(kl_current_user=current_user)

	Session(app)

	import klima.common.database as database
	database.init_app(app)

	import klima.views.home as home
	import klima.views.pet as pet
	import klima.views.species as species
	app.register_blueprint(home.bp)
	app.register_blueprint(pet.bp)
	app.register_blueprint(species.bp)

	return app
