from flask import (
	Blueprint, flash, g, redirect, render_template,
    request, session, url_for
)

bp = Blueprint('home', __name__, url_prefix='/')

@bp.route('/')
def index():
	return render_template("home/index.html")

@bp.route('/register', methods=('POST', 'GET'))
def register():
	return render_template("home/register.html")

@bp.route('/login', methods=('POST', 'GET'))
def login():
	return render_template("home/login.html")
