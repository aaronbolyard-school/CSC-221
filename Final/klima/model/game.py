from klima.common.auth import current_user
from klima.model.klimamon import Klimamon
from klima.model.user import User
from klima.model.userWeather import UserWeather
from klima.model.species import Species
from klima.model.main import db

def get_current_weather():
	user = current_user()
	return UserWeather.get(user)

def get_current_pet():
	user = current_user()
	if user:
		return Klimamon.query.filter_by(user_id=user.id).first()
	return None

def has_pet():
	return get_current_pet() != None

def give_pet(name, species):
	name = name.strip()
	if len(name) == 0:
		return False

	user = current_user()
	if not user:
		return False, 

	pet = get_current_pet()
	if pet:
		db.session.delete(pet)

	pet = Klimamon(user_id=user.id, species_id=species.id, name=name)
	db.session.add(pet)
	db.session.commit()

	return pet
