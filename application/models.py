from application import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, current_user
from sqlalchemy.sql import text

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


class Result(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	#description = db.Column(db.String(144))
	session_id = db.Column(db.Integer, db.ForeignKey('session.id'))

	def __init__(self, description):
		self.description = description

class Conditioning(Result):
	id = db.Column(db.ForeignKey("result.id"), primary_key=True)
	#workout = db.Column(db.String, nullable=False) #tämä kun on luotu workouts-taulu
	distance = db.Column(db.Integer, nullable=False) #tän ois hyvä olla 5 10 tai 50m välein???
	time = db.Column(db.DateTime, nullable=False)

class Session(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	date = db.Column(db.Date, default=db.func.current_date(), nullable=False)
	account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

	results = db.relationship("Result", backref='session', lazy=True)

	@staticmethod
	def count_sessions_last_30_days():
		stmt = text("SELECT COUNT(DISTINCT date) FROM session WHERE date  BETWEEN date('now', '-30 days') AND date("
					"'now', 'localtime') AND account_id =" + str(current_user.id) + ";")
		res = db.engine.execute(stmt)
		result = []
		for row in res:
			result.append(row[0])

		return result[0]

	@staticmethod
	def count_sessions():
		stmt = text("SELECT COUNT(*) FROM session;")
		res = db.engine.execute(stmt)
		result = []
		for row in res:
			result.append(row[0])

		return result[0]

