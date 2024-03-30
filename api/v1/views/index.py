#!/usr/bin/python3
"""Index module"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status')
def hbnb_status():
    """show status as a json"""
    status = jsonify(status="OK")
    return status


@app_views.route('/stats')
def hbnb_stats():
    from models.amenity import Amenity
    from models.city import City
    from models.place import Place
    from models.review import Review
    from models.state import State
    from models.user import User
    """Returns the number of each objects by type"""
    return jsonify({"amenities": storage.count(Amenity),
                    "cities": storage.count(City),
                    "places": storage.count(Place),
                    "reviews": storage.count(Review),
                    "states": storage.count(State),
                    "users": storage.count(User)})
