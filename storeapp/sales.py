from flask_restful import Resource
from flask_restful import fields
from flask_restful import reqparse
from flask_restful import abort
from flask_restful import Api
from flask_restful.reqparse import RequestParser
from flask import request, jsonify

sales = [
    {
        "sale_id": 1,
        "name" : "tops",
	    "qty_sold" : 2,
	    "amount" : 10000,
	    "product_id" : 4,
	    "category" : "clothes"
    },
    {
        "sale_id": 2,
        "name" : "hats",
	    "qty_sold" : 3,
	    "amount" : 15000,
	    "product_id" : 3,
	    "category" : "clothes"
    }

]

def get_sale_by_id(sale_id):
    for sale in sales:
        if sale.get("sale_id") == int(sale_id):
            return sale


sale_request_parser = RequestParser(bundle_errors=True)
sale_request_parser.add_argument("sale_id", type=int, required=True, help="Please enter a valid integer for sale_id.")
sale_request_parser.add_argument("product_name", type=str, required=True, help="Product_name has to be a valid string")
sale_request_parser.add_argument("qty_sold", type=int, required=True, help="Please enter a valid integer for qty_sold")
sale_request_parser.add_argument("amount", type=int, required=True, help="Please enter a valid integer for amount")
sale_request_parser.add_argument("product_id", type=int, required=True, help="Please enter a valid integer for product_id")
sale_request_parser.add_argument("category", type=str, required=True, help="Category has to be a val  id string")

class sale:
    def __init__(self, sale_id, product_name, qty_sold, amount, product_id, category):
        self.sale_id = sale_id
        self.product_name = product_name
        self.qty_sold = qty_sold
        self.amount = amount
        self.product_id = product_id
        self.category = category

class SaleOne(Resource):
    def get(self, sale_id):
        sale = get_sale_by_id(sale_id)
        if not sale:
            return {"error": "sale not found"} 
        return sale

class SaleList(Resource):
    def get(self):
        return sales

    # create a new sale and add it to sales.
    def post(self):
        sales.append(request.get_json())
        return {"msg": "Sale has been made."}, 201