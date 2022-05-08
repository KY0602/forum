from . import db
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.String(255), primary_key=True)
    username = db.Column(db.String(45))
    email = db.Column(db.String(45))
    password = db.Column(db.String(255))
    description = db.Column(db.String(255))
    profile_photo = db.Column(db.Text)

    following = db.relationship(
        'User',
        lambda: RelationUserFollowed,
        primaryjoin=lambda: User.user_id == RelationUserFollowed.c.user_id_follower,
        secondaryjoin=lambda: User.user_id == RelationUserFollowed.c.user_id_followed,
        backref='followers'
    )

    blocking = db.relationship(
        'User',
        lambda: RelationUserBlocked,
        primaryjoin=lambda: User.user_id == RelationUserBlocked.c.user_id_blocker,
        secondaryjoin=lambda: User.user_id == RelationUserBlocked.c.user_id_blocked,
        backref='blockers'
    )


RelationUserFollowed = db.Table(
    'relation_user_followed', Base.metadata,
    db.Column('user_id_follower', db.String(255), db.ForeignKey(User.user_id), primary_key=True),
    db.Column('user_id_followed', db.String(255), db.ForeignKey(User.user_id), primary_key=True)
)

RelationUserBlocked = db.Table(
    'relation_user_blocked', Base.metadata,
    db.Column('user_id_blocker', db.String(255), db.ForeignKey(User.user_id), primary_key=True),
    db.Column('user_id_blocked', db.String(255), db.ForeignKey(User.user_id), primary_key=True)
)

class Status(db.Model):
    __tablename__ = 'status'
    id = db.Column(db.String(255), primary_key=True)
    user_id = db.Column(db.String(255))
    type = db.Column(db.String(45))
    title = db.Column(db.String(255))
    text = db.Column(db.Text)
    media = db.Column(db.Text)
    location = db.Column(db.Text)
    date_created = db.Column(db.DateTime)
    like = db.Column(db.Integer, default=0)
    like_users = db.Column(db.Text)

