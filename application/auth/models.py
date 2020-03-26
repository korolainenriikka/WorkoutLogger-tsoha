from application import db
from werkzeug.security import generate_password_hash


class User(db.Model):
    __tablename__ = "account"

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False, unique=True)
    password_hash = db.Column(db.String(144), nullable=True)

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True
