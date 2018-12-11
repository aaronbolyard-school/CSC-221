from klima.model.main import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Text)
	password = db.Column(db.Text)
	email = db.Column(db.Text, unique=True)
	zip = db.Column(db.Text)

	def __repr__(self):
		return '<User %r>' % self.name
