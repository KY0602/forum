from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_apscheduler import APScheduler
import configparser

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    config = configparser.RawConfigParser()
    config.read('config.cfg')
    db_dict = dict(config.items('DATABASE'))
    app.config["SECRET_KEY"] = db_dict["secret_key"]
    app.config["SQLALCHEMY_DATABASE_URI"] = db_dict["db"]
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    from .users import users as users_blueprint
    app.register_blueprint(users_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app