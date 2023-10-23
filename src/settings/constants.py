from os import getenv
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()
redis_broker = getenv("REDIS_BROKER")
redis_master = getenv("REDIS_MASTER")
config = {
    "SQLALCHEMY_DATABASE_URI": getenv("DATABASE_URL"),
    "SQLALCHEMY_TRACK_MODIFICATIONS": True,
    "SECRET_KEY": getenv("SECRET_KEY"),
    "broker_url": redis_broker,
    "broker_transport_options": {
        'master_name': redis_master,
        'sentinels': [(redis_broker, 26379)],
    },
    "result_backend": redis_broker,
    "result_backend_transport_options": {
        'master_name': redis_master,
        'sentinels': [(redis_broker, 26379)],
    },
    "accept_content": ["application/json"],
    "result_serializer": "json",
    "task_serializer": "json",
    "timezone": "UTC",
    "beat_schedule":{
        'periodic-every-60-seconds': {
            'task': 'periodic',
            'schedule': timedelta(seconds=60),
            # 'args': (param1, param2, param3) if wanna pass arguments
        },
    }
}
