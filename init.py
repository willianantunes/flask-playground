import logging.config

from flask import Flask

from flask_playground.config.settings import FLASK_DEBUG
from flask_playground.config.settings import HOST
from flask_playground.config.settings import LOGGING
from flask_playground.config.settings import PORT
from flask_playground.routes.v1 import api_v1_routes

app = Flask(__name__)
app.register_blueprint(api_v1_routes, url_prefix="/api")

if __name__ == "__main__":
    logging.config.dictConfig(LOGGING)
    app.run(debug=FLASK_DEBUG, host=HOST, port=PORT)
