from . import db


class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.String(255), primary_key=True)
    username = db.Column(db.String(45))
    email = db.Column(db.String(45))
    password = db.Column(db.String(255))
    description = db.Column(db.String(255))
