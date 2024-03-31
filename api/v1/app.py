#!/usr/bin/python3
"""flask app for rendering api"""
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from flask_cors import CORS

api_config = {"origins": ["0.0.0.0"]}

app = Flask(__name__)
app.url_map.strict_slashes = False
app.register_blueprint(app_views)
CORS(app,
     resources={r"/*": api_config})


@app.teardown_appcontext
def tearDown_appcontext(exception):
    """Calls stroage.close to release storage engine resources"""
    storage.close()


@app.errorhandler(404)
def page_not_found(e):
    """404 error handler"""
    return jsonify(error="Not found"), 404


if __name__ == "__main__":
    from os import getenv
    HBNB_API_HOST = getenv('HBNB_API_HOST') or '0.0.0.0'
    HBNB_API_PORT = getenv('HBNB_API_PORT') or 5000
    app.run(debug=True, host=HBNB_API_HOST, port=HBNB_API_PORT, threaded=True)
