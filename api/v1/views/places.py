#!/usr/bin/python3
"""Place view Module"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from werkzeug.exceptions import BadRequest
from models.place import Place


@app_views.route('/cities/<string:city_id>/places', methods=['GET'],
                 strict_slashes=False)
def get_place(city_id):
    """get places as a json"""
    city = storage.get("City", city_id)
    if city is None:
        abort(404)
    places_list = [place.to_dict() for place in city.places]
    return jsonify(places_list)


@app_views.route('/places/<string:place_id>', methods=['GET'],
                 strict_slashes=False)
def get_places(place_id):
    """get places as a json"""
    place = storage.get("Place", place_id)
    if place is None:
        abort(404)
    return jsonify(place.to_dict())


@app_views.route('/places/<string:place_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_place(place_id):
    """delete places as a json"""
    place = storage.get("Place", place_id)
    if place is None:
        abort(404)
    place.delete()
    storage.save()
    return jsonify({}), 200


@app_views.route('/cities/<string:city_id>/places', methods=['POST'],
                 strict_slashes=False)
def create_place(city_id):
    """create places as a json"""

    city = storage.get("City", city_id)
    if city is None:
        abort(404)

    req_data = request.get_json()

    if req_data is None:
        raise BadRequest(description="Not a JSON")
    if req_data.get("user_id", None) is None:
        raise BadRequest(description="Missing user_id")

    user_id = req_data.get("user_id")
    user = storage.get("User", user_id)
    if user is None:
        abort(404)
    if req_data.get("name", None) is None:
        raise BadRequest(description="Missing name")

    name = req_data.get("name")
    place = Place(city_id=city_id, user_id=user_id, name=name)
    place.save()
    return jsonify(place.to_dict()), 201


@app_views.route('/places/<string:place_id>', methods=['PUT'],
                 strict_slashes=False)
def update_place(place_id):
    """create places as a json"""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    req_data = request.get_json()
    if req_data is None:
        raise BadRequest(description="Not a JSON")
    keys_ignore = ["id", "user_id", "city_id", "created_at", "updated_at"]
    for key, value in req_data.items():
        if key not in keys_ignore:
            setattr(place, key, value)
    place.save()
    return jsonify(place.to_dict()), 200
