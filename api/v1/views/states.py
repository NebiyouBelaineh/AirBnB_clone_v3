#!/usr/bin/python3
"""State module"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from werkzeug.exceptions import BadRequest


@app_views.route('/states', strict_slashes=False, methods=['GET'])
def get_states():
    """get states as a json"""
    states = storage.all("State")
    states_list = []
    for state in states.values():
        states_list.append(state.to_dict())
    return jsonify(states_list)


@app_views.route('/states/<string:state_id>',
                 strict_slashes=False, methods=['GET'])
def get_state(state_id):
    """get states as a json"""
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    return jsonify(state.to_dict())


@app_views.route('/states/<string:state_id>',
                 strict_slashes=False, methods=['DELETE'])
def delete_state(state_id):
    """delete states as a json"""
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    state.delete()
    storage.save()
    return jsonify({}), 200


@app_views.route('/states',
                 strict_slashes=False, methods=['POST'])
def create_state():
    """create states as a json"""
    from models.state import State
    req_data = request.get_json()
    if req_data is None:
        raise BadRequest(description="Not a JSON")
    if req_data.get("name", None) is None:
        raise BadRequest(description="Missing name")
    name = req_data.get("name")
    state = State(name=name)
    state.save()
    return jsonify(state.to_dict()), 201
