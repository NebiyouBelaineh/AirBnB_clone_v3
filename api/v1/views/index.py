#!/usr/bin/python3
"""Index module"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', strict_slashes=False)
def status():
    """show status as a json"""
    status = jsonify({"status": "OK"})
    return status


@app_views.route('/stats', strict_slashes=False)
def stats():
    """Returns the number of each objects by type"""

    from models import storage
    from models.amenity import Amenity
    from models.city import City
    from models.place import Place
    from models.review import Review
    from models.state import State
    from models.user import User

    classes = {"amenities": Amenity, "cities": City, "places": Place,
               "reviews": Review, "states": State, "users": User}

    obj = {}
    for key, values in classes.items():
        obj[key] = storage.count(values)
    return jsonify(obj)
