from vhs.model.main import db
from vhs.model.customer import Customer
from vhs.model.movie import Movie
from datetime import datetime

class Rental(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	day_rented = db.Column(db.Date, default=datetime.now())

	movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), nullable=False)
	movie = db.relationship('Movie', foreign_keys=[movie_id])

	customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
	customer = db.relationship('Customer', foreign_keys=[customer_id])

	def compute_statement(rentals):
		frequent_renter_points = 0
		total_amount = 0

		now = datetime.now().date()

		for rental in rentals:
			difference = now - rental.day_rented

			current_amount = 0
			if rental.movie.price_code == Movie.PRICE_REGULAR:
				current_amount += 2
				if difference.days > 2:
					current_amount += (difference.days - 2) * 1.5
			elif rental.movie.price_code == Movie.PRICE_NEW:
				current_amount += difference.days * 3
			elif rental.movie.price_code == Movie.PRICE_CHILDREN:
				current_amount += 1.5
				if difference.days > 3:
					current_amount += (difference.days - 3) * 1.5

			frequent_renter_points += 1
			if rental.movie.price_code == Movie.PRICE_NEW and difference.days > 1:
				frequent_renter_points += 1

			total_amount += current_amount

		return total_amount, frequent_renter_points

	def __repr__(self):
		return '<Rental %s>' % str(self.day_rented)