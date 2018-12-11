from flask import (
	Blueprint, flash, g, redirect, render_template,
    request, session, url_for
)

from klima.common.auth import user_required
from klima.common.database import flush_database, get_database
from klima.model.species import Species
import klima.model.game as Game

bp = Blueprint('pet', __name__, url_prefix='/pet')

@bp.route('/select', methods=("GET", "POST"))
@bp.route('/select/<int:species_id>', methods=("GET", "POST"))
@user_required
def select(species_id=None):
	if Game.has_pet():
		return redirect(url_for("pet.view"))

	if species_id != None:
		species = Species.query.filter_by(id=species_id).first()
		if not species:
			flash("Species not found.")
		else:
			pet = Game.give_pet(species.name, species)
			if not pet:
				flash("Couldn't assign pet.")

			return redirect(url_for("pet.view"))

	species = Species.query.all()
	return render_template("pet/select.html", species=species)

@bp.route('/view')
@user_required
def view():
	weather = Game.get_current_weather()
	pet = Game.get_current_pet()

	if not pet:
		return redirect(url_for("pet.select"))
	else:
		return render_template("pet/view.html", weather=weather, pet=pet)

@bp.route('/change', methods=('GET','POST'))
@user_required
def change():
	return "change pet"
