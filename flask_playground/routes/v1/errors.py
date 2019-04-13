from flask import jsonify

from flask_playground.routes.exceps import ValidationError
from flask_playground.routes.v1 import api_v1_routes


@api_v1_routes.errorhandler(ValidationError)
def bad_request(e):
    response = jsonify({"message": e.args[0]})
    response.status_code = 400
    return response


@api_v1_routes.app_errorhandler(404)
def not_found(e):
    response = jsonify({"message": "Invalid resource URI"})
    response.status_code = 404
    return response


@api_v1_routes.errorhandler(405)
def method_not_supported(e):
    response = jsonify({"message": "The method is not supported"})
    response.status_code = 405
    return response


@api_v1_routes.app_errorhandler(500)
def internal_server_error(e):
    response = jsonify({"error": "Internal server error", "message": e.args[0]})
    response.status_code = 500
    return response
