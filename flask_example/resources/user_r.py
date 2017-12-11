from flask import jsonify
from flask_restful import Resource
from flask_example.models import User


class UserResource(Resource):
    def get(self, id=None):
        # Tranh truong hop truyen id = 0
        if id is not None:
            user = User.query.filter_by(id=id).first()
            return jsonify(user.as_dict())
