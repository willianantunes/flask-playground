import logging

from flask import jsonify
from flask import request

from flask_playground.business import user_dealer
from flask_playground.routes.exceps import ValidationError
from flask_playground.routes.v1 import api_v1_routes

logger = logging.getLogger(__name__)


@api_v1_routes.route("/v1/users/eligible")
def eligible_to_be_contacted():
    username = request.args.get("username")

    if not username:
        raise ValidationError("Username is needed to avaluate its eligibility")

    logger.info(f"Verifying eligibility for {username}")
    result = user_dealer.is_eligible(username)

    return jsonify({"eligibility": result})
