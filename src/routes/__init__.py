from flask import Blueprint
from .v1 import tasks_api

routes = Blueprint('routes', __name__)

routes.register_blueprint(tasks_api, url_prefix='/v1')