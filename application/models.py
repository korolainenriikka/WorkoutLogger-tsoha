from application import db
from werkzeug.security import generate_password_hash
from flask_login import UserMixin, current_user
from sqlalchemy.sql import text

class User(UserMixin, db.Model):
	__tablename__ = "account"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(144), nullable=False)
	username = db.Column(db.String(144), nullable=False, unique=True)
	password_hash = db.Column(db.String(144), nullable=True)

	results = db.relationship("Session", backref='account', lazy=True)

	def __init__(self, name, username, password):
		self.name = name
		self.username = username
		self.password_hash = generate_password_hash(password)


class Result(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	description = db.Column(db.String(144))
	session_id = db.Column(db.Integer, db.ForeignKey('session.id'))

	def __init__(self, description):
		self.description = description

class Session(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	date = db.Column(db.Date, default=db.func.date())
	account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=True)

	results = db.relationship("Result", backref='session', lazy=True)

	@staticmethod
	def count_sessions_last_30_days():
		stmt = text("SELECT COUNT(DISTINCT date) FROM session WHERE date  BETWEEN date('now', '-30 days') AND date("
					"'now', 'localtime') AND account_id =" +  str(current_user.id) + ";")
		res = db.engine.execute(stmt)
		result = []
		for row in res:
			result.append(row[0])

		return result[0]