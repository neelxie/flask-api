from flask_restful import Resource
from flask_restful import fields
from flask_restful import reqparse
from flask_restful import abort
from flask_restful import Api
from flask_restful.reqparse import RequestParser
from flask import request, jsonify

users = []

def get_user_by_username(username):
    for user in users:
        return user if user.get("username") == username
            

user_request_parser = RequestParser(bundle_errors=True)
user_request_parser.add_argument("username", type=str, required=True, help="Name has to be valid string.")
user_request_parser.add_argument("role", type=str, required=True, help="Role has to be a valid string")

class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role
        self.password = 'password'

class UserOne(Resource):
    def get(self, username):
        user = get_user_by_username(username)
        return {"error": "User not found"} if not user else user

class UserList(Resource):
    def get(self):
        return users

    def post(self):
        pass