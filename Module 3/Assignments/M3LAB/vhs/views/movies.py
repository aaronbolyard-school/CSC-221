from flask import (
	Blueprint, flash, g, redirect, render_template,
    request, session, url_for
)

from vhs.common.database import get_database
from vhs.model.movie import Movie

bp = Blueprint('movies', __name__, url_prefix='/movies')

@bp.route('/')
def index():
	movies = Movie.query.order_by(Movie.id.desc()).limit(5).all()
	
	return render_template('movies/index.html',movies=movies)

@bp.route('/delete/<int:id>')
def delete(id):
	database = get_database()

	try:
		database.session.delete(Movie.query.filter_by(id=id).first())
		database.session.commit()
	
		flash("Deleted movie.")
	except:
		flash("Failed to delete movie.")

	return redirect(url_for("movies.index"))

@bp.route('/edit/<int:id>', methods=('GET', 'POST'))
def edit(id):
	database = get_database()

	movie = Movie.query.filter_by(id=id).first()

	if not movie:
		flash("Movie doesn't exist.")
		return redirect(url_for("movies.index"))

	if request.method == 'POST':
		movie.title = request.form.get('title', "")

		try:
			movie.price_code = int(request.form.get('price_code', "0"))
		except:
			flash("Please select a valid price code.")

		database.session.add(movie)
		database.session.commit()
	
		flash("Updated movie.")
		
	return render_template("movies/edit.html", movie=movie, Movie=Movie)

@bp.route('/add')
def add():
	database = get_database()

	try:
		movie = Movie(title='New Movie')
		database.session.add(movie)
		database.session.commit()

		return redirect(url_for("movies.edit", id=movie.id))
	except:
		flash("Failed to add movie.")

	return redirect(url_for("movies.index"))
