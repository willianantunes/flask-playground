import os
from logging import Formatter

from pythonjsonlogger.jsonlogger import JsonFormatter

HOST = os.getenv("WA_HOST", "0.0.0.0")
PORT = int(os.getenv("WA_PORT", 8000))

FLASK_DEBUG = os.getenv("WA_FLASK_DEBUG", True)

GITHUB_GRAPHQL_ENDPOINT = os.getenv("WA_GITHUB_GRAPHQL_ENDPOINT")
GITHUB_API_TOKEN = os.getenv("WA_GITHUB_API_TOKEN")

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "std-json-formatter": {
            "()": JsonFormatter,
            "format": "%(levelname)-8s [%(asctime)s] [%(request_id)s] %(name)s: %(message)s",
        },
        "std-formatter": {"()": Formatter, "format": "%(asctime)s - level=%(levelname)s - %(name)s - %(message)s"},
    },
    "handlers": {
        "console": {"class": "logging.StreamHandler", "formatter": os.getenv("WA_LOG_FORMATTER", "std-formatter")}
    },
    "loggers": {
        "": {"level": os.getenv("WA_ROOT_LOG_LEVEL", "INFO"), "handlers": ["console"]},
        "flask_playground": {
            "level": os.getenv("WA_PROJECT_LOG_LEVEL", "INFO"),
            "handlers": ["console"],
            "propagate": False,
        },
        "flask": {"level": os.getenv("WA_FLASK_LOG_LEVEL", "DEBUG"), "propagate": False, "handlers": ["console"]},
    },
}
