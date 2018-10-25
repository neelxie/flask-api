from flask import Blueprint, jsonify, request
from flask_restful import Api
from storeapp.products import ProductList
from storeapp.products import ProductOne
from storeapp.sales import SaleList
from storeapp.sales import SaleOne
from storeapp.users import UserOne
from storeapp.users import UserList
from storeapp.index import Index


api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(Index, '/')
api.add_resource(ProductList, '/Products')
api.add_resource(ProductOne, '/Products/<int:product_id>')
api.add_resource(SaleList, '/Sales')
api.add_resource(SaleOne, '/Sales/<int:sale_id>')
api.add_resource(UserList, '/Users')
api.add_resource(UserOne, '/Users/<string:username>')