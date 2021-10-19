import os

APP_ENV = os.environ.get("APP_ENV", "development")

DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_DATABASE")

ELASTIC_HOST = "localhost"
ELASTIC_PORT = "9200"
