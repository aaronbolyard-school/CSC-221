from klima.model.main import db

class Klimamon(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Text)

	user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
	user = db.relationship(
		"User",
		backref=db.backref("user", cascade="all, delete-orphan"),
		foreign_keys=[user_id])

	species_id = db.Column(db.Integer, db.ForeignKey("species.id"))
	species = db.relationship(
		"Species",
		backref=db.backref("species", cascade="all, delete-orphan"),
		foreign_keys=[species_id])

	def __repr__(self):
		return '<Klimamon %r of %r>' % self.user.name % self.species.id