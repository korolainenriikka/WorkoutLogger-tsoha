from application import db
from werkzeug.security import generate_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model):
	__tablename__ = "account"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(144), nullable=False)
	username = db.Column(db.String(144), nullable=False, unique=True)
	password_hash = db.Column(db.String(144), nullable=True)

	results = db.relationship("Result", backref='account', lazy=True)

	def __init__(self, name, username, password):
		self.name = name
		self.username = username
		self.password_hash = generate_password_hash(password)


class Result(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	date = db.Column(db.DateTime, default=db.func.current_timestamp())
	description = db.Column(db.String(144))

	account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=True)

	def __init__(self, description):
		self.description = description
