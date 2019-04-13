from flask import Blueprint

api_v1_routes = Blueprint("api_v1", __name__)

from . import users, errors  # isort:skip
