# import os, json

from flask import Flask
from flask_cors import CORS
from . import routes
from . import config

def create_app():
    app = Flask(__name__)
    CORS(app)

    with app.app_context():

        app.config.from_object(config.Config)

        app.register_blueprint(routes.routes)

    return app

app = create_app()