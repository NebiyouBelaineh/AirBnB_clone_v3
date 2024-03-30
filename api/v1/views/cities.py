#!/usr/bin/python3
"""City view Module"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from werkzeug.exceptions import BadRequest


@app_views.route('/states/<string:state_id>/cities', methods=['GET'])
def get_cities_by_state(state_id):
    """get cities as a json"""
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    cities_list = [city.to_dict() for city in state.cities]
    return jsonify(cities_list)


@app_views.route('/cities/<string:city_id>', methods=['GET'])
def get_cities(city_id):
    """get cities as a json"""
    city = storage.get("City", city_id)
    if city is None:
        abort(404)
    return jsonify(city.to_dict())


@app_views.route('/cities/<string:city_id>', methods=['DELETE'])
def delete_city(city_id):
    """delete cities as a json"""
    cities = storage.get("City", city_id)
    if cities is None:
        abort(404)
    cities.delete()
    storage.save()
    return jsonify({}), 200


@app_views.route('/states/<string:state_id>/cities', methods=['POST'])
def create_city(state_id):
    """create cities as a json"""
    from models.state import State
    from models.city import City
    states = storage.all("State")
    state_found = None
    for state in states.values():
        if state.id == state_id:
            state_found = state
            break
    if state_found is None:
        abort(404)
    req_data = request.get_json()
    if req_data is None:
        raise BadRequest(description="Not a JSON")
    if req_data.get("name", None) is None:
        raise BadRequest(description="Missing name")

    city = City(**req_data)
    city.save()
    return jsonify(city.to_dict()), 201


@app_views.route('/cities/<string:city_id>', methods=['PUT'])
def update_city(city_id):
    """update city as a json"""
    from models.city import City
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    req_data = request.get_json()
    if req_data is None:
        raise BadRequest(description="Not a JSON")
    keys_ignore = ["id", "state_id", "created_at", "updated_at"]
    for key, value in req_data.items():
        if key not in keys_ignore:
            setattr(city, key, value)
    city.save()
    return jsonify(city.to_dict()), 200
