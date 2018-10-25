from flask_restful import Resource
from flask_restful import fields
from flask_restful import reqparse
from flask_restful import abort
from flask_restful import Api
from flask_restful.reqparse import RequestParser
from flask import request, jsonify
from storeapp.models.sales_model import sale

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