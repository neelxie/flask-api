from flask import Blueprint, jsonify, request
from flask_restful import Api
from storeapp.views.products_view import ProductList
from storeapp.views.products_view import ProductOne
from storeapp.views.sales_view import SaleList
from storeapp.views.sales_view import SaleOne
from storeapp.views.index import Index


api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(Index, '/')
api.add_resource(ProductList, '/Products')
api.add_resource(ProductOne, '/Products/<int:product_id>')
api.add_resource(SaleList, '/Sales')
api.add_resource(SaleOne, '/Sales/<int:sale_id>')