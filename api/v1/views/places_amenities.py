#!/usr/bin/python3
"""Place view Module"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from werkzeug.exceptions import BadRequest
from models.review import Review
from models import storage_t


@app_views.route('/places/<string:place_id>/amenities', methods=['GET'],
                 strict_slashes=False)
def get_amenities_place(place_id):
    """Returns amenities linked to a place object"""
    place = storage.get("Place", place_id)
    if place is None:
        abort(404)
    if storage_t == 'db':
        amenities_list = [amenity.to_dict() for amenity in place.amenities]
    else:
        amenities_list = [(storage.get("Amenity", amenity_id).to_dict()
                           for amenity_id in place.amenity_ids)]
    return jsonify(amenities_list)


@app_views.route('/places/<string:place_id>/amenities/<string:amenity_id>',
                 methods=['POST'], strict_slashes=False)
def create_place_amenity(place_id, amenity_id):
    """Creates an amenity for a place object"""
    place = storage.get("Place", place_id)
    if place is None:
        abort(404)
    amenity = storage.get("Amenity", amenity_id)
    if amenity is None:
        abort(404)

    if storage_t == 'db':
        if amenity in place.amenities:
            return jsonify(amenity.to_dict()), 200
        else:
            place.amenities.append(amenity)
            place.save()
            return jsonify(amenity.to_dict()), 201
    else:
        if amenity.id in place.amenity_ids:
            return jsonify(amenity.to_dict()), 200
        else:
            place.amenity_ids.append(amenity.id)
            place.save()
            return jsonify(amenity.to_dict()), 201


@app_views.route('/places/<string:place_id>/amenities/<string:amenity_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_place_amenity(place_id, amenity_id):
    """Deletes an amenity for a place object"""
    place = storage.get("Place", place_id)
    if place is None:
        abort(404)
    amenity = storage.get("Amenity", amenity_id)
    if amenity is None:
        abort(404)
    if storage_t == 'db':
        if amenity not in place.amenities:
            abort(404)
        else:
            amenity.delete()
            storage.save()
            return jsonify({}), 200
    else:
        if amenity not in place.amenity_ids:
            abort(404)
        else:
            place.amenity_ids.remove(amenity.id)
            storage.save()
            return jsonify({}), 200
