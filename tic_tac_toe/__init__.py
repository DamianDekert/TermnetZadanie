import os

from flask import Flask
from flask_session import Session
from flask_smorest import Api

from .resources.board import blp as BoardBlueprint
from .resources.main import blp as MainBlueprint
from .resources.statistic import blp as StatisticBlueprint
from .events import socketio
from .db import db
from tic_tac_toe.models import UserStatistic, UserModel

from datetime import timedelta


def create_app(db_url=None):
    app = Flask(__name__)

    # https://flask-smorest.readthedocs.io/en/latest/api_reference.html
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
    app.config["API_TITLE"] = "Kółko i krzyżyk"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"

    # Connection use ElephantSQL

    app.config["SQLALCHEMY_DATABASE_URI"] = \
        db_url or os.getenv("DATABASE_URL", "sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    app.config["SESSION_TYPE"] = 'sqlalchemy'
    app.config["SESSION_SQLALCHEMY"] = db
    app.permanent_session_lifetime = timedelta(minutes=30)

    socketio.init_app(app)
    db.init_app(app)
    api = Api(app)
    Session(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(BoardBlueprint)
    app.register_blueprint(MainBlueprint)
    app.register_blueprint(StatisticBlueprint)

    return app
