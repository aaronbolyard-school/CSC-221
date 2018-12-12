from flask import (
	Blueprint, flash, g, redirect, render_template,
    request, session, url_for
)

import klima.common.auth
from klima.common.database import flush_database, get_database
from klima.model.klimamon import Klimamon
import klima.model.game as Game

bp = Blueprint('home', __name__, url_prefix='/')

@bp.route('/')
def index():
	from klima.model.user import User
	from klima.model.userWeather import UserWeather

	user = User.query.filter_by(id=1).first()
	weather = None
	if user:
		weather = UserWeather.get(user)
	else:
		weather = {}

	return render_template("home/index.html", weather=weather)

@bp.route('/register', methods=('GET','POST'))
def register():
	user = klima.common.auth.current_user()
	if user:
		return redirect(url_for("home.index"))

	form = {}
	if request.method == 'POST':
		name = request.form.get('name', "").strip()
		zip_code = request.form.get('zip', "").strip()
		email = request.form.get('email', "").strip()
		confirm_email = request.form.get('confirm-email', "").strip()
		password = request.form.get('password', "").strip()
		confirm_password = request.form.get('confirm-password', "").strip()

		error = False
		if email != confirm_email:
			flash("Emails don't match.")
			error = True
		if password != confirm_password:
			flash("Passwords don't match.")
			error = True
		if len(name) == 0:
			flash("Please enter a name.")
			error = True
		if len(zip_code) == 0:
			flash("Please enter a zip code.")
			error = True

		result = klima.common.auth.create(email, password)
		if result == klima.common.auth.USERNAME_INVALID:
			flash("Email already used.")
			error = True
		elif result == klima.common.auth.PASSWORD_INVALID:
			flash("Password not strong enough.")
			error = True

		if not error:
			db = get_database()
			flush_database()
			klima.common.auth.login(email, password)

			user = klima.common.auth.current_user()
			user.name = name
			user.zip = zip_code
			db.session.add(user)
			flush_database()

			flash("Succesfully created account!")
			return redirect(url_for("home.index"))

		form['name'] = name
		form['zip'] = zip_code
		form['email'] = email

	return render_template("home/register.html", form=form)

@bp.route('/login', methods=('GET','POST'))
def login():
	user = klima.common.auth.current_user()
	if user:
		return redirect(url_for("home.index"))

	form = {}
	if request.method == 'GET':
		form['url'] = request.args.get('url', "")
	elif request.method == 'POST':
		email = request.form.get('email', "").strip()
		password = request.form.get('password', "").strip()

		result = klima.common.auth.login(email, password)
		error = True
		if result == klima.common.auth.USERNAME_INVALID:
			flash("Email invalid.")
		elif result == klima.common.auth.PASSWORD_INVALID:
			flash("Password invalid.")
		elif result == klima.common.auth.VERIFICATION_PENDING:
			flash("Verification still pending.")
		else:
			error = False

		if not error:
			url = request.form.get('url', "").strip()
			if len(url) > 0:
				return redirect(request.form['url'])
			else:
				return redirect(url_for("home.index"))

		form['email'] = email

	return render_template("home/login.html", form=form)


@bp.route('/logout')
@klima.common.auth.user_required
def logout():
	klima.common.auth.logout()

	return redirect(url_for("home.index"))

@bp.route('/go')
@klima.common.auth.user_required
def go():
	if Game.has_pet():
		return redirect(url_for("pet.view"))
	else:
		return redirect(url_for("pet.select"))
