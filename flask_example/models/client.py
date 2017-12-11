from .base import ExampleBase
from flask_example.extensions import db


class Client(ExampleBase):
    __talbename__ = 'client'
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User',
                           backref=db.backref('clients', lazy=True))
