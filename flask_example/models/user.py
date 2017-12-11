from flask_example.extensions import db
from .base import ExampleBase


class User(ExampleBase):
    __tablename__ = 'user'
    username = db.Column(db.String(40), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True)
