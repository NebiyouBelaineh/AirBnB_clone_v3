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


@app_views.route('/places_search', methods=['POST'],
                 strict_slashes=False)
def places_search():
    """Searches for places based on json request body"""
    req_data = request.get_json()
    if req_data is None:
        raise BadRequest(description="Not a JSON")

    state_ids = req_data.get("states", None)
    city_ids = req_data.get("cities", None)
    amenity_ids = req_data.get("amenities", None)
    places_list = []
    p_states = []
    p_cities = []

    # Get all places in states
    if state_ids is not None:
        for state_id in state_ids:
            current_state = storage.get("State", state_id)
            for city in current_state.cities:
                for place in city.places:
                    if amenity_ids is None:
                        p_states.append(place)
                    else:
                        for amenity_id in amenity_ids:
                            for amnty in place.amenities:
                                if amenity_id == amnty.id:
                                    p_states.append(place)

    # Get all places in cities that are not already included
    if city_ids is not None:
        for c_id in city_ids:
            current_city = storage.get("City", c_id)
            if current_city:
                for place in current_city.places:
                    if amenity_ids is None and place not in p_states:
                        p_cities.append(place)
                    else:
                        for amenity_id in amenity_ids:
                            for amnty in place.amenities:
                                if (amenity_id
                                    == amnty.id
                                    and place
                                    not in
                                        p_states):
                                    p_cities.append(place)
    for place in p_states:
        places_list.append(place.to_dict())
    for place in p_cities:
        places_list.append(place.to_dict())
    # Delets amenities key that includes all amenities objects
    for p in places_list:
        if p.get('amenities'):
            del p['amenities']

    return jsonify(places_list), 200
