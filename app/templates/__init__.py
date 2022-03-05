from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from app import config_options


app = Flask(__name__)

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)

def create_app(config_name):
    app.config.from_object(config_options[config_name])

    return app