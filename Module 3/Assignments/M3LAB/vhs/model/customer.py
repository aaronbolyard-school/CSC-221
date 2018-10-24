from vhs.model.main import db

class Customer(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Text, nullable=False)

	def __repr__(self):
		return '<Customer %r>' % self.name
