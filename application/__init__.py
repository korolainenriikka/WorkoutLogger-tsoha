# flask app
from flask import Flask
app = Flask(__name__)

# database
from flask_sqlalchemy import SQLAlchemy
import os
if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///wologger.db"
    app.config["SQLALCHEMY_ECHO"] = True
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# migration
from flask_migrate import Migrate
migrate = Migrate(app, db)

# login
from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager, current_user

login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to view this functionality"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# user types
from flask_principal import Principal, Permission, RoleNeed, UserNeed, identity_loaded

principal = Principal(app)
admin_permission = Permission(RoleNeed('admin'))

@identity_loaded.connect_via(app)
def on_identity_loaded(sender, identity):
    identity.user = current_user
    if hasattr(current_user, 'id'):
        identity.provides.add(UserNeed(current_user.id))
        identity.provides.add(RoleNeed(current_user.user_type))

# app
from application import views
from application.auth import views, models, forms
from application.auth.manage_users import views
from application.result import models, forms
from application.result.log import views
from application.result.analyze import views

# create db
db.create_all()
