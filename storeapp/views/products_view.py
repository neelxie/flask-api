from flask_restful import Resource
from flask_restful import fields
from flask_restful import reqparse
from flask_restful import abort
from flask_restful import Api
from flask_restful.reqparse import RequestParser
from flask import request, jsonify
from storeapp.models.products_model import Product
from storeapp.authenticate import AuthenticateViews

auth_obj = AuthenticateViews()
products = [
    {
        "name" : "tops",
	    "qty" : 12,
	    "min_stock" : 23,
	    "price" : 311,
	    "units" : 50,
	    "category" : "clothes",
        "product_id": 1
    },
    {
        "name" : "shorts",
	    "qty" : 9,
	    "min_stock" : 30,
	    "price" : 1000,
	    "units" : 15,
	    "category" : "clothes",
        "product_id": 2
    }
]

def get_product_by_id(product_id):
    for product in products:
        if product.get("product_id") == int(product_id):
            return product
            

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
        data = request.get_json()
        data["product_id"] = len(products)+ 1
        prod_keys = ("name","qty","min_stock","price","units","category")
        if all(key in data.keys() for key in prod_keys):
            name = data.get("name")
            qty = data.get("qty")
            min_stock = data.get("min_stock")
            price = data.get("price")
            units = data.get("units")
            category = data.get("category")

            not_valid = auth_obj.authenticate_product(name, qty, min_stock, price, units, category)
            if not_valid:
                return {"msg": not_valid}, 400
            products.append(data)
            return {"msg": "Product has been added."}, 201
        return {"msg": "Stuff missng"}