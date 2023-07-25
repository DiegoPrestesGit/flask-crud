from flask_restful import Api
from app import flask_app_instance
from .user import User
from .user_by_id import UserById

rest_server = Api(flask_app_instance)
rest_server.add_resource(User, '/api/python/user')
rest_server.add_resource(UserById, '/api/python/user/<string:user_id>')
