import os

HOST = os.getenv("WA_HOST", "0.0.0.0")
PORT = int(os.getenv("WA_PORT", 8000))

FLASK_DEBUG = os.getenv("WA_FLASK_DEBUG", True)

GITHUB_GRAPHQL_ENDPOINT = os.getenv("WA_GITHUB_GRAPHQL_ENDPOINT")
GITHUB_API_TOKEN = os.getenv("WA_GITHUB_API_TOKEN")
