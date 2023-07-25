from flask_restful import Resource
import logging as logger
from .database import get_all_users, create_user
from flask import request


class User(Resource):
    def get(self):
        users = get_all_users()
        return users, 200

    def post(self):
        body = request.get_json()
        if not body:
            return {"message": "nothing to see here"}, 400

        user_name = body.get('name')
        user_email = body.get('email')
        user_password = body.get('password')

        new_user = create_user(user_name, user_email, user_password)
        return new_user, 201
