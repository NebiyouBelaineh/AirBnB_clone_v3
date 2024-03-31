#!/usr/bin/python3
"""Place view Module"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from werkzeug.exceptions import BadRequest
from models.review import Review


@app_views.route('/places/<string:place_id>/reviews', methods=['GET'],
                 strict_slashes=False)
def get_reviews_place(place_id):
    """get reviews as a json"""
    place = storage.get("Place", place_id)
    if place is None:
        abort(404)
    reviews_list = [review.to_dict() for review in place.reviews]
    return jsonify(reviews_list)


@app_views.route('/reviews/<string:review_id>', methods=['GET'],
                 strict_slashes=False)
def get_review(review_id):
    """get places as a json"""
    review = storage.get("Review", review_id)
    if review is None:
        abort(404)
    return jsonify(review.to_dict())


@app_views.route('/reviews/<string:review_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_review(review_id):
    """delete places as a json"""
    review = storage.get("Review", review_id)
    if review is None:
        abort(404)
    review.delete()
    storage.save()
    return jsonify({}), 200


@app_views.route('/places/<string:place_id>/reviews', methods=['POST'],
                 strict_slashes=False)
def create_review(place_id):
    """create places as a json"""

    place = storage.get("Place", place_id)
    if place is None:
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
    if req_data.get("text", None) is None:
        raise BadRequest(description="Missing text")

    text = req_data.get("text")
    review = Review(place_id=place_id, user_id=user_id, text=text)
    review.save()
    return jsonify(review.to_dict()), 201


@app_views.route('/reviews/<string:review_id>', methods=['PUT'],
                 strict_slashes=False)
def update_review(review_id):
    """create places as a json"""
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)
    req_data = request.get_json()
    if req_data is None:
        raise BadRequest(description="Not a JSON")
    keys_ignore = ["id", "user_id", "place_id", "created_at", "updated_at"]
    for key, value in req_data.items():
        if key not in keys_ignore:
            setattr(review, key, value)
    review.save()
    return jsonify(review.to_dict()), 200
