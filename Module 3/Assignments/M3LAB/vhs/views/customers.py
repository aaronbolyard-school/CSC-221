from flask import (
	Blueprint, flash, g, redirect, render_template,
    request, session, url_for
)

from vhs.model.customer import Customer
from vhs.common.database import get_database

bp = Blueprint('customers', __name__, url_prefix='/customers')

@bp.route('/')
def index():
	customers = Customer.query.order_by(Customer.id.desc()).all()
	
	return render_template('customers/index.html',customers=customers)

@bp.route('/delete/<int:id>')
def delete(id):
	database = get_database()

	try:
		database.session.delete(Customer.query.filter_by(id=id).first())
		database.session.commit()
	
		flash("Deleted customer.")
	except:
		flash("Failed to delete customer.")

	return redirect(url_for("customers.index"))

@bp.route('/edit/<int:id>', methods=('GET', 'POST'))
def edit(id):
	database = get_database()

	customer = Customer.query.filter_by(id=id).first()

	if not customer:
		flash("Customer doesn't exist.")
		return redirect(url_for("customers.index"))

	if request.method == 'POST':
		customer.name = request.form.get('name', "")

		database.session.add(customer)
		database.session.commit()
	
		flash("Updated customer.")
		
	return render_template("customers/edit.html", customer=customer, Customer=Customer)

@bp.route('/add')
def add():
	database = get_database()

	customer = Customer(name='Bob Smith')
	database.session.add(customer)
	database.session.commit()

	return redirect(url_for("customers.edit", id=customer.id))
