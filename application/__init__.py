# flask-sovellus
from flask import Flask
app = Flask(__name__)

# tietokanta
from flask_sqlalchemy import SQLAlchemy
import os
if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///wologger.db"
    app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

# migraatio
from flask_migrate import Migrate
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

migrate = Migrate(app, db)

# kirjautuminen
from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to view this functionality"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# oma sovellus
from application import views

from application.results import models
from application.results import views

from application.auth import models
from application.auth import views

#luodaan tietokantataulut
db.create_all()
