from flask_restful import Resource
from flask_restful import fields
from flask_restful import reqparse
from flask_restful import abort
from flask_restful import Api
from flask_restful.reqparse import RequestParser
from flask import request, jsonify

products = [
    {
        "product_id": 1,
        "name" : "tops",
	    "qty" : 12,
	    "min_stock" : 23,
	    "price" : 311,
	    "units" : 50,
	    "category" : "clothes"
    },
    {
        "product_id": 2,
        "name" : "tops",
	    "qty" : 12,
	    "min_stock" : 23,
	    "price" : 311,
	    "units" : 50,
	    "category" : "clothes"
    }
]

def get_product_by_id(product_id):
    for product in products:
        if product.get("product_id") == int(product_id):
            return product 
            

product_request_parser = RequestParser(bundle_errors=True)
product_request_parser.add_argument("product_id", type=int, required=True, help="Please enter a valid integer for id.")
product_request_parser.add_argument("name", type=str, required=True, help="name has to be a valid string")
product_request_parser.add_argument("qty", type=int, required=True, help="Please enter a valid integer for qty")
product_request_parser.add_argument("min_stock", type=int, required=True, help="Please enter a valid integer for min_stock")
product_request_parser.add_argument("price", type=int, required=True, help="Please enter a valid integer for price")
product_request_parser.add_argument("units", type=int, required=True, help="Please enter a valid integer for units")
product_request_parser.add_argument("category", type=str, required=True, help="Category has to be a valid string")

class Product:
    def __init__(self, product_id, name, qty, min_stock, price, units, category):
        self.product_id = product_id
        self.name = name
        self.qty = qty
        self.min_stock = min_stock
        self.price = price
        self.units = units
        self.category = category 

class ProductOne(Resource):
    def get(self, product_id):
        product = get_product_by_id(product_id)
        if not product:
            return {"error": "product not found"} 
        return product

class ProductList(Resource):
    def get(self):
        return products

    # create a new product and add it to products.
    def post(self):
        products.append(request.get_json())
        return {"msg": "Product has been added."}, 201