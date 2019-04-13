import os

FLASK_DEBUG = os.getenv("WA_FLASK_DEBUG", True)
HOST = os.getenv("WA_HOST", "0.0.0.0")
PORT = int(os.getenv("WA_PORT", 8000))
