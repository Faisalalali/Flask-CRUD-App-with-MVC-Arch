from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    phone = db.Column(db.String, nullable=True)

    def __init__(self, name, email, password, phone):
        self.name = name
        self.email = email
        self.password = password
        self.phone = phone

    def __repr__(self):
        return f"{self.user_id}-{self.name}:{self.email}"
