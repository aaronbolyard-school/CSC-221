from flask import (
	Blueprint, flash, g, redirect, render_template,
    request, session, url_for
)

from vhs.common.database import get_database
from vhs.model.customer import Customer
from vhs.model.movie import Movie
from vhs.model.rental import Rental
from datetime import date

bp = Blueprint('rentals', __name__, url_prefix='/rentals')

@bp.route('/customer/<int:id>')
def customer(id):
	rentals = Rental.query.filter_by(customer_id=id).all()
	customer = Customer.query.filter_by(id=id).first()

	total_amount, frequent_renter_points = Rental.compute_statement(rentals)

	return render_template(
		'rentals/customer.html',
		rentals=rentals,
		customer=customer,
		total_amount=total_amount,
		frequent_renter_points=frequent_renter_points)

@bp.route('/delete/<int:id>')
def delete(id):
	database = get_database()
	rental = Rental.query.filter_by(id=id).first()
	if rental:
		customer_id = rental.customer.id
		database.session.delete(rental)
		database.session.commit()

		flash('Deleted rental.')
		return redirect(url_for('rentals.customer', id=customer_id))
	else:
		flash("Rental not found.")
		return redirect(url_for('customers.index'))

@bp.route('/update/<int:id>', methods=('POST','GET'))
def update(id):
	database = get_database()
	rental = Rental.query.filter_by(id=id).first()

	if rental:
		if request.method == 'POST':
			year = request.form.get("year", rental.day_rented.year)
			month = request.form.get("month", rental.day_rented.month)
			day = request.form.get("day", rental.day_rented.day)

			try:
				rental.day_rented = date(int(year), int(month), int(day))
			except:
				flash("Invalid date specified.")

			database.session.add(rental)
			database.session.commit()

			flash("Rental updated.")
			return redirect(url_for('rentals.customer', id=rental.customer.id))

		return render_template('rentals/update.html', rental=rental)
	else:
		flash("Rental not found.")
		return redirect(url_for('customers.index'))

@bp.route('/add/movie/<int:id>')
def add_movie(id):
	movies = Movie.query.order_by(Movie.title.asc()).all()
	customer = Customer.query.filter_by(id=id).first()

	return render_template('rentals/add.html', movies=movies, customer=customer)

@bp.route('/add/assign/<int:customer_id>/<int:movie_id>')
def add_assign(customer_id, movie_id):	
	database = get_database()
	rental = Rental(customer_id=customer_id, movie_id=movie_id)
	database.session.add(rental)
	database.session.commit()

	flash("Added rental.")
	return redirect(url_for('rentals.customer', id=customer_id))
