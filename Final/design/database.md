# User
* ID: int; primary key
* Password: text
* Email: text
* Name: text
* Zip: text

# UserWeather
* userID: int, foreign key to User
* rain: real
* snow: real
* wind: real
* temp: real
* cloud: real
* timeToLive: Date

# Klimamon
* ID: int; primary key
* userID: int, foreign key for User
* speciesID: int, foreign key for Species
* name: text

# Species
* ID: int; primary key
* resource: text; url to Klimamon JSON
