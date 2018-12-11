from flask import (
	Blueprint, flash, g, redirect, render_template,
    request, session, url_for, current_app, Response
)

import os, errno
from klima.common.auth import user_required
from klima.common.database import flush_database, get_database
from klima.model.species import Species

bp = Blueprint('species', __name__, url_prefix='/species')

@bp.route('/view/<int:id>')
def view(id):
	path = os.path.join(current_app.instance_path, 'species', str(id))
	try:
		with current_app.open_resource(path) as file:
			data = file.read()
			mime = "application/json"

			return Response(data, content_type=mime)
	except Exception as e:
		return Response(
			"{ \"message\": \"species not found\" }",
			content_type="application/json")

def make_directory(path):
	try:
		os.makedirs(path)
	except OSError as e:
		if e.errno == errno.EEXIST and os.path.isdir(path):
			pass
		else:
			raise

@bp.route('/add', methods=('GET','POST'))
@bp.route('/add/<int:id>', methods=('GET','POST'))
@user_required
def add(id=None):
	form = {}

	if request.method == 'POST':
		name = request.form.get("name", "").strip()

		error = False
		file = None
		if not 'file' in request.files:
			flash("Warning: no file uploaded.")
		if len(name) == 0:
			flash("No name provided.")
			error = True
		
		file = None
		if not error and 'file' in request.files:
			file = request.files['file']
			if file.filename == "":
				flash("Please select a file to upload.")
				error = True

		if not error:
			db = get_database()
			species = None
			if id:
				species = Species.query.filter_by(id=id).first()
				if species:
					species.name = name
			if not species:
				species = Species(name=name)
			db.session.add(species)
			db.session.commit()

			if file:
				root_path = os.path.join(current_app.instance_path, "species")
				make_directory(root_path)

				file_path = os.path.join(root_path, str(species.id))
				file.save(file_path)

			flash("Added species %r." % name)

		form['name'] = name
	else:
		if id:
			species = Species.query.filter_by(id=id).first()
			if species:
				form['name'] = species.name

	return render_template("species/add.html", form=form)

@bp.route('/')
@bp.route('/list')
@user_required
def list():
	species = Species.query.all()
	return render_template("species/list.html", species=species)

@bp.route('/delete/<int:id>', methods=('GET','POST'))
@user_required
def delete(id):
	return "delete species %d" % id
