#!/usr/bin/python3
from models import storage
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.city import City

amenity1 = Amenity(name="Fridge")
amenity1.save()
amenity2 = Amenity(name="Wifi")
amenity2.save()
amenity3 = Amenity(name="TV")
amenity3.save()
amenity4 = Amenity(name="Kitchen")
amenity4.save()
state1 = State(name="Illinois")
state1.save()
city1 = City(state_id=state1.id, name="Chicago")
city1.save()
city2 = City(state_id=state1.id, name="Bewyn")
city2.save()

user1 = User(email="dridi.chaith@gmail.com", password="1234", first_name="Dridi", last_name="Chaith")
user1.save()
place1 = Place(city_id=city1.id, user_id=user1.id, name="Chicago sweet home", description="Beautiful home of your dreams", number_rooms=3, number_bathrooms=1, max_guest=3, price_by_night=25, latitude=235.325, longitude=32.14)
review1 = Review(place_id=place1.id, user_id=user1.id, text="Best home ever")

city1.places.append(place1)

place1.reviews.append(review1)
place1.amenities.append(amenity1)
place1.amenities.append(amenity2)
place1.amenities.append(amenity3)
place1.amenities.append(amenity4)
place1.save()
review1.save()
state1.cities.append(city1)
state1.cities.append(city2)
