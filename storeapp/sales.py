from flask_restful import Resource
from flask_restful import fields
from flask_restful import reqparse
from flask_restful import abort
from flask_restful import Api
from flask_restful.reqparse import RequestParser
from flask import request, jsonify

sales = []

def get_sale_by_id(sale_id):
    for sale in sales:
        if sale.get("sale_id") == int(sale_id):
            return sale


sale_request_parser = RequestParser(bundle_errors=True)
sale_request_parser.add_argument("sale_id", type=int, required=True, help="Please enter a valsale_id integer for sale_id.")
sale_request_parser.add_argument("name", type=str, required=True, help="name has to be a valsale_id string")
sale_request_parser.add_argument("qty_sold", type=int, required=True, help="Please enter a valsale_id integer for qty_sold")
sale_request_parser.add_argument("amount", type=int, required=True, help="Please enter a valsale_id integer for amount")
sale_request_parser.add_argument("product_id", type=int, required=True, help="Please enter a valsale_id integer for product_id")
sale_request_parser.add_argument("category", type=str, required=True, help="Category has to be a valsale_id string")

class sale:
    def __init__(self, sale_id, name, qty_sold, amount, product_id, category):
        self.sale_id = sale_id
        self.name = name
        self.qty_sold = qty_sold
        self.amount = amount
        self.product_id = product_id
        self.category = category

class SaleOne(Resource):
    def get(self, sale_id):
        sale = get_sale_by_id(sale_id)
        return {"error": "sale not found"} if not sale else sale

class SaleList(Resource):
    def get(self):
        return sales

    # create a new sale and add it to sales.
    def post(self):
        sales.append(request.get_json())
        return {"msg": "Sale has been made."}, 201