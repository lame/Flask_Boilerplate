from mixins import CRUDMixin
from flask.ext.login import UserMixin
from flask.ext.sqlalchemy import SQLAlchemy
from app import db

ROLE_USER = 0
ROLE_ADMIN = 1

class User(UserMixin, CRUDMixin,  db.Model):

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20), unique = True)
    password = db.Column(db.String(20))
    lastSeen = db.Column(db.DateTime)
    
    role = db.Column(db.SmallInteger, default = ROLE_USER)
    db = db.relationship('Database', backref='user', lazy='dynamic')

    def __init__(self, name=None, password=None):
        self.name = name
        self.password = password

    def is_active(self):
        return True

    def get_id(self):
        return unicode(self.id)

    def is_admin(self):
        if self.role > 0:
            return True
        else:
            return False

    def __repr__(self):
        return '<User %r>' % (self.name)

class Database(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    name = db.Column(db.String(255), unique = True)

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<Database %r>' % (self.name)
