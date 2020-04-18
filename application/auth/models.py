from flask_login import UserMixin
from sqlalchemy import text
from werkzeug.security import generate_password_hash, check_password_hash

from application import db


class User(UserMixin, db.Model):
	__tablename__ = "account"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(144), nullable=False)
	username = db.Column(db.String(144), nullable=False, unique=True)
	user_type = db.Column(db.String(144))
	password_hash = db.Column(db.String(144))

	results = db.relationship("Session", backref='account', lazy=True)

	def __init__(self, name, username, password, user_type='user'):
		self.name = name
		self.username = username
		self.password_hash = generate_password_hash(password)
		self.user_type = user_type

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)

	@staticmethod
	def count_users():
		stmt = text("SELECT COUNT(*) FROM account;")
		res = db.engine.execute(stmt)
		result = []
		for row in res:
			result.append(row[0])

		return result[0]


class Usergroup(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(144), nullable=False)


class UserUsergroup(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('account.id'))
	usergroup_id = db.Column(db.Integer, db.ForeignKey('usergroup.id'))
