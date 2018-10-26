from flask_restful.reqparse import RequestParser


class Product:
    def __init__(self, product_id, name, qty, min_stock, price, units, category):
        self.product_id = product_id
        self.name = name
        self.qty = qty
        self.min_stock = min_stock
        self.price = price
        self.units = units
        self.category = category 


product_request_parser = RequestParser(bundle_errors=True)
product_request_parser.add_argument("product_id", type=int, required=True, help="Please enter a valid integer for id.")
product_request_parser.add_argument("name", type=str, required=True, help="name has to be a valid string")
product_request_parser.add_argument("qty", type=int, required=True, help="Please enter a valid integer for qty")
product_request_parser.add_argument("min_stock", type=int, required=True, help="Please enter a valid integer for min_stock")
product_request_parser.add_argument("price", type=int, required=True, help="Please enter a valid integer for price")
product_request_parser.add_argument("units", type=int, required=True, help="Please enter a valid integer for units")
product_request_parser.add_argument("category", type=str, required=True, help="Category has to be a valid string")