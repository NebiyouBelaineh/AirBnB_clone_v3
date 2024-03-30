#!/usr/bin/python3
"""Index module"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', strict_slashes=False)
def hbnb_status():
    """show status as a json"""
    status = jsonify(status="OK")
    return status


@app_views.route('/stats', strict_slashes=False)
def hbnb_stats():
    """Returns the number of each objects by type"""
    classes = {"amenities": 'Amenity',
               "cities": 'City',
               "places": 'Place',
               "reviews": 'Review',
               "states": 'State',
               "users": 'User'}

    obj = {}
    for key, values in classes.items():
        obj[key] = storage.count(values)
    return jsonify(obj)
