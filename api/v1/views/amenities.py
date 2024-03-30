#!/usr/bin/python3
"""Amenity view Module"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from werkzeug.exceptions import BadRequest


@app_views.route('/amenities', methods=['GET'],
                 strict_slashes=False)
def get_amenities():
    """get amenities as a json"""
    amenities = storage.all("Amenity")
    amenities_list = []
    for amenity in amenities.values():
        amenities_list.append(amenity.to_dict())
    return jsonify(amenities_list)


@app_views.route('/amenities/<string:amenity_id>', methods=['GET'],
                 strict_slashes=False)
def get_amenity(amenity_id):
    """get amenities as a json"""
    amenity = storage.get("Amenity", amenity_id)
    if amenity is None:
        abort(404)
    return jsonify(amenity.to_dict())


@app_views.route('/amenities/<string:amenity_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_amenity(amenity_id):
    """delete amenities as a json"""
    amenity = storage.get("Amenity", amenity_id)
    if amenity is None:
        abort(404)
    amenity.delete()
    storage.save()
    return jsonify({}), 200


@app_views.route('/amenities', methods=['POST'],
                 strict_slashes=False)
def create_amenity():
    """create amenities as a json"""
    from models.amenity import Amenity
    req_data = request.get_json()
    if req_data is None:
        raise BadRequest(description="Not a JSON")
    if req_data.get("name", None) is None:
        raise BadRequest(description="Missing name")
    name = req_data.get("name")
    amenity = Amenity(name=name)
    amenity.save()
    return jsonify(amenity.to_dict()), 201


@app_views.route('/amenities/<string:amenity_id>', methods=['PUT'],
                 strict_slashes=False)
def update_amenity(amenity_id):
    """create amenities as a json"""
    from models.amenity import Amenity
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    req_data = request.get_json()
    if req_data is None:
        raise BadRequest(description="Not a JSON")
    keys_ignore = ["id", "created_at", "updated_at"]
    for key, value in req_data.items():
        if key not in keys_ignore:
            setattr(amenity, key, value)
    amenity.save()
    return jsonify(amenity.to_dict()), 200
