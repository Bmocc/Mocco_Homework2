from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
from os import environ

load_dotenv(".flaskenv")

app = Flask(__name__)
app.config["SECRET_KEY"] = "csc330"

DB_NAME = environ.get("SQLITE_DB")
base_dir = os.path.abspath(os.path.dirname(__file__))
DB_CONFIG_STR = "sqlite:///" + os.path.join(base_dir, DB_NAME)
app.config["SQLALCHEMY_DATABASE_URI"] = DB_CONFIG_STR
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)

from app import routes, forms, models
from app.models import CityTime, Country, City

with app.app_context():
    # Create DB schema
    db.create_all()

