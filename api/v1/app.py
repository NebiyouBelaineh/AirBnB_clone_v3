#!/usr/bin/python3
"""flask app for rendering api"""
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def tearDown_appcontext(exception):
    """Calls stroage.close to release storage engine resources"""
    storage.close()


@app.errorhandler(404)
def page_not_found(e="Not found"):
    """404 error handler"""
    return jsonify(error=str(e)), 404


if __name__ == "__main__":
    HBNB_API_HOST = getenv('HBNB_API_HOST') or '0.0.0.0'
    HBNB_API_PORT = getenv('HBNB_API_PORT') or 5000
    app.run(debug=True, host=HBNB_API_HOST, port=HBNB_API_PORT, threaded=True)
