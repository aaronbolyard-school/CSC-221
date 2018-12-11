from klima.model.main import db

class Species(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	resource = db.Column(db.Text)
	name = db.Column(db.Text)

	def __repr__(self):
		return '<Species %r>' % self.name
