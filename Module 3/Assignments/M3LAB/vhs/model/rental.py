from vhs.model.main import db

class Rental(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	days_rented = db.Column(db.Integer, default=1)

	movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), nullable=False)
	movie = db.relationship('Movie', foreign_keys=[movie_id])

	customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
	customer = db.relationship('Customer', foreign_keys=[customer_id])

	def __repr__(self):
		return '<Rental %d days>' % self.days_rented