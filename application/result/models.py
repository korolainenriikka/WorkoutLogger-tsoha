from application import db
from flask_login import current_user
from sqlalchemy.sql import text

import os


class Session(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	date = db.Column(db.Date, default=db.func.current_date(), nullable=False)
	account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

	results = db.relationship("Result", backref='session', lazy=True)

	@staticmethod
	def count_sessions_last_30_days():
		if os.environ.get("HEROKU"):
			stmt = text("SELECT COUNT(DISTINCT date) FROM session WHERE date > current_date - interval "
						"'30' AND account_id = :id;")
		else:
			stmt = text("SELECT COUNT(DISTINCT date) FROM session WHERE date BETWEEN date('now', '-30 days') AND date("
					"'now', 'localtime') AND account_id = :id;")

		res = db.engine.execute(stmt, id=current_user.id)
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


class Result(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	session_id = db.Column(db.Integer, db.ForeignKey('session.id'))

class Conditioning(Result):
	id = db.Column(db.ForeignKey("result.id"), primary_key=True)
	distance = db.Column(db.Integer, nullable=False)
	time = db.Column(db.Time, nullable=False)
	workout_id = db.Column(db.Integer, db.ForeignKey('session.id'))

	@staticmethod
	def find_personal_bests():
		stmt = text("SELECT date, distance, min(time) AS time FROM Conditioning "
					"JOIN result ON conditioning.id=result.id JOIN session ON session.id=session_id "
					"WHERE account_id = 1 GROUP BY session.date, distance;")

		res = db.engine.execute(stmt, id=current_user.id)
		result = []
		for row in res:
			result.append((row[0], row[1], row[2]))

		return result

class Strength(Result):
	id = db.Column(db.ForeignKey("result.id"), primary_key=True)
	reps = db.Column(db.Integer, nullable=False)
	weight = db.Column(db.Integer, nullable=False)
	workout_id = db.Column(db.Integer, db.ForeignKey('workout.id'))

class Workout(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(144), nullable=False)