from flask_restful import Resource
from flask_restful import fields
from flask_restful import reqparse
from flask_restful import abort
from flask_restful import Api
from flask_restful.reqparse import RequestParser

products = [
    {
        'id': 1,
        'name': 'Pens',
        'qty': 231,
        'Min-Stock': 200,
        'price': 700,
        'Units': 3000,
        'category': 'stationary'    
    },
    {
        'id': 2,
        'name': 'soaks',
        'qty': 23,
        'Min-Stock': 20,
        'price': 1500,
        'Units': 30,
        'category': 'clothes'
    }
]
def get_product_by_name(name):
    for product in products:
        if product.get("name") == name:
            return product


product_request_parser = RequestParser(bundle_errors=True)
product_request_parser.add_argument("id", type=int, required=True, help="Please enter a valid integer for id.")
product_request_parser.add_argument("name", type=str, required=True, help="name has to be a valid string")
product_request_parser.add_argument("qty", type=int, required=True, help="Please enter a valid integer for qty")
product_request_parser.add_argument("min_stock", type=int, required=True, help="Please enter a valid integer for min_stock")
product_request_parser.add_argument("price", type=int, required=True, help="Please enter a valid integer for price")
product_request_parser.add_argument("units", type=int, required=True, help="Please enter a valid integer for units")
product_request_parser.add_argument("category", type=str, required=True, help="Category has to be a valid string")

class Product:
    def __init__(self, id, name, qty, min_stock, price, units, category):
        self.id = id
        self.name = name
        self.qty = qty
        self.min_stock = min_stock
        self.price = price
        self.units = units
        self.category = category

class ProductOne(Resource):
    def get(self, name):
        product = get_product_by_name(name)
        if not product:
            return {"error": "product not found"}
        return product

class ProductList(Resource):
    def get(self):
        return products

    def post(self):
        args = product_request_parser.parse_args()
        products.append(args)
        return {"msg": "product added", "product_info": args}
