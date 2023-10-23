from os import getenv
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Blueprint

db = SQLAlchemy()
migrate = Migrate()
router = Blueprint("router", __name__)
redis_broker = getenv("REDIS_BROKER")
redis_master = getenv("REDIS_MASTER")
config = {
    "SQLALCHEMY_DATABASE_URI": getenv("DATABASE_URL"),
    "SQLALCHEMY_TRACK_MODIFICATIONS": True,
    "SECRET_KEY": getenv("SECRET_KEY"),
    "broker_url": redis_broker,
    "CELERY_BROKER_TRANSPORT_OPTIONS": {
        'master_name': redis_master,
        'sentinels': [(redis_broker, 26379)],
    },
    "result_backend": redis_broker,
    "CELERY_RESULT_BACKEND_TRANSPORT_OPTIONS": {
        'master_name': redis_master,
        'sentinels': [(redis_broker, 26379)],
    },
    "accept_content": ["application/json"],
    "result_serializer": "json",
    "task_serializer": "json",
    "timezone": "UTC"
}
