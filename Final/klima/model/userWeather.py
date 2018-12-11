import math
import requests
from flask import current_app
from datetime import datetime, timedelta
from klima.model.main import db

class UserWeather(db.Model):
	id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
	time = db.Column(db.DateTime, default=datetime.now())
	rain = db.Column(db.Float)
	snow = db.Column(db.Float)
	wind = db.Column(db.Float)
	temp = db.Column(db.Float)
	cloud = db.Column(db.Float)
	user = db.relationship(
		"User",
		backref=db.backref("items", cascade="all, delete-orphan"),
		foreign_keys=[id])

	def __repr__(self):
		return '<UserWeather %r>' % self.user.name

	def refresh(self, force=False):
		current_time = datetime.now()
		if self.time + timedelta(hours=1) < current_time or force:
			result = requests.get("https://api.openweathermap.org/data/2.5/weather?zip=%s,us&units=imperial&APPID=%s" % (self.user.zip, current_app.config['OPEN_WEATHER_MAP_KEY']))
			json = result.json()
			self.time = current_time

			main = json.get('main', {})
			self.temp = math.floor(main.get('temp', 0))

			self.rain = 0
			rain = json.get('rain', None)
			if rain:
				if rain.get('1h', False):
					self.rain = math.floor(rain['1h'])
				elif rain.get('3h', False):
					self.rain = math.floor(rain['3h'])

			self.snow = 0
			snow = json.get('snow', None)
			if snow:
				if snow.get('1h', False):
					self.snow = math.floor(snow['1h'])
				elif snow.get('3h', False):
					self.snow = math.floor(snow['3h'])

			wind = json.get('wind', {})
			self.wind = wind.get('speed', 0)

			clouds = json.get('clouds', {})
			self.cloud = clouds.get('all', 0)

			db.session.add(self)

	def get(user, force=False):
		weather = UserWeather.query.filter_by(id=user.id).first()
		if not weather:
			weather = UserWeather(id=user.id)

			db.session.add(weather)
			db.session.commit()

			weather.refresh(True)
			db.session.commit()
		else:
			weather.refresh(force)

		return weather
