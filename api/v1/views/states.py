#!/usr/bin/python3
"""State module"""
from api.v1.views import app_views
from flask import jsonify, abort
from models import storage


@app_views.route('/states', strict_slashes=False, methods=['GET'])
def get_states():
    """get states as a json"""
    states = storage.all("State")
    states_list = []
    for state in states.values():
        states_list.append(state.to_dict())
    return jsonify(states_list)


@app_views.route('/states/<string:state_id>', strict_slashes=False, methods=['GET'])
def get_state(state_id):
    """get states as a json"""
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    return jsonify(state.to_dict())

@app_views.route('/states/<string:state_id>', strict_slashes=False, methods=['DELETE'])
def delete_state(state_id):
    """delete states as a json"""
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    state.delete()
    storage.save()
    return jsonify({}), 200

