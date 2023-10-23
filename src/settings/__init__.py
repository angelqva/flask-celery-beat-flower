import os
from flask import Flask
from celery import Celery
from settings import constants
# from .extensions import db
# from .views import main
# from .utils import make_celery


def make_celery(app):
    celery = Celery(app.import_name)
    celery.conf.update(constants.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery


def create_app():
    app = Flask(__name__)
    app.config.update(constants.config)
    constants.db.init_app(app)
    constants.migrate.init_app(app, constants.db)
    celery = make_celery(app)
    celery.set_default()
    app.register_blueprint(constants.router)

    return app, celery
