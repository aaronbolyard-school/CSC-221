import functools
import click
from flask import (
	Flask, current_app, session, redirect, url_for,
	flash, render_template, request
)
from werkzeug.security import (
	check_password_hash, generate_password_hash
)

from klima.common.database import get_database
from klima.model.user import User

SUCCESS              = 0
USERNAME_INVALID     = 1
PASSWORD_INVALID     = 2
VERIFICATION_PENDING = 3
FAILED               = 4

MIN_PASSWORD_LENGTH = 10

def login(email, password):
	"""
	Logs in the user with the email and password.

	* Returns USERNAME_INVALID if no user with that name exists.
	* Returns PASSWORD_INVALID if the password is not valid.
	* Returns VERIFICATION_PENDING if the user needs verified.
	* Returns SUCCESS if the user was successfully logged in.
	"""
	db = get_database()
	user = User.query.filter_by(email=email).first()
	if user:
		if check_password_hash(user.password, password):
			session.clear()
			session['user_id'] = user.id

			return SUCCESS
		else:
			return PASSWORD_INVALID
	else:
		return USERNAME_INVALID

def create(email, password, invalidate=True):
	"""
	Creates a user with the provided email and password.

	Returns USERNAME_INVALID if email is already taken. Returns
	VERIFICATION_PENDING if the user needs validated. Returns PASSWORD_INVALID
	if the password does not meet the requirements. Otherwise, returns SUCCESS
	if the user was successfully created.
	"""

	email = email.strip()
	password = password.strip()

	if len(password) < MIN_PASSWORD_LENGTH:
		return PASSWORD_INVALID

	user = User.query.filter_by(email=email).first()
	if user:
		return USERNAME_INVALID
	else:
		user = User()
		user.password = generate_password_hash(password)
		user.email = email

		db = get_database()
		db.session.add(user)
		return SUCCESS

def current_user():
	"""
	Gets the current user, or None if no user is signed in.
	"""
	user_id = session.get('user_id', None)
	if user_id != None:
		return User.query.filter_by(id=user_id).first()
	return None

def logout():
	"""
	Logs the current user out.
	"""
	session.clear()

def user_required(view):
	@functools.wraps(view)
	def wrapped_view(**kwargs):
		user = current_user()
		if user == None:
			flash("You must be logged in to view this page.")
			return redirect(url_for('home.login' ,url=request.url))

		return view(**kwargs)

	return wrapped_view
