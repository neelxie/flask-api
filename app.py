from flask import Blueprint, jsonify, request
from flask_restful import Api
from storeapp.products import ProductList
from storeapp.products import ProductOne
#from resources.Sales import Sales

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

#from storeapp.Users import UserOne
#from storeapp.Users import UserList

api.add_resource(ProductList, '/Products')
api.add_resource(ProductOne, '/Products/<string:name>')
#api.add_resource(Sales, '/Sales')
#api.add_resource(Sales, '/Sales/<int:sale_id>', endpoint)
#api.add_resource(Users, '/Users')
#api.add_resource(UserList, '/Users')
#api.add_resource(UserOne, '/Users/<string:username>')