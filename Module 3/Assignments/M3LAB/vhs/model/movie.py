from vhs.model.main import db

class Movie(db.Model):
	PRICE_REGULAR  = 0
	PRICE_CHILDREN = 1
	PRICE_NEW      = 2

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.Text, nullable=False)
	price_code = db.Column(db.Integer, nullable=False, default=PRICE_REGULAR)

	def __repr__(self):
		return '<Movie %r>' % self.title
