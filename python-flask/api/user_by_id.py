from flask_restful import Resource
import logging as logger
from .database import get_user_by_id


class UserById(Resource):
    def get(self, user_id):
        selected_user = get_user_by_id(user_id)
        return selected_user, 200
