#!/usr/bin/python3
""" Script that imports a Blueprint and runs Flask """
from flask import Flask, make_response, jsonify
from flask_cors import CORS
from models import storage
from api.v1.views import app_views
import os
from flasgger import Swagger

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


app.register_blueprint(app_views, url_prefix="/api/v1")


@app.errorhandler(404)
def page_not_found(e):
    return {"error": "Not found"}, 404


@app.errorhandler(400)
def page_not_found(e):
    message = e.description
    return message, 400


@app.teardown_appcontext
def close(ctx):
    storage.close()


if os.getenv("HBNB_API_HOST"):
    host = os.getenv("HBNB_API_HOST")
else:
    host = "0.0.0.0"

if os.getenv("HBNB_API_PORT"):
    port = int(os.getenv("HBNB_API_PORT"))
else:
    port = 5000


if __name__ == "__main__":
    app.run(host=host, port=port, threaded=True)
