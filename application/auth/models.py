from flask_login import UserMixin
from sqlalchemy import text
from werkzeug.security import generate_password_hash, check_password_hash

from application import db

class Usergroup(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(144), nullable=False)


db.Table('UserUsergroup',
    db.Column('user_id', db.Integer, db.ForeignKey('account.id'), primary_key=True),
    db.Column('usergroup_id', db.Integer, db.ForeignKey('usergroup.id'), primary_key=True)
)

class User(UserMixin, db.Model):
	__tablename__ = "account"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(144), nullable=False)
	username = db.Column(db.String(144), nullable=False, unique=True)
	password_hash = db.Column(db.String(144))

	results = db.relationship("Session", backref='account', lazy=True)
	usergroups = db.relationship("Usergroup",
							secondary="UserUsergroup", backref=db.backref('usergroup', lazy='dynamic'))

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



