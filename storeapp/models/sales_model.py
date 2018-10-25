from flask_restful.reqparse import RequestParser


class sale:
    def __init__(self, sale_id, product_name, qty_sold, amount, product_id, category):
        self.sale_id = sale_id
        self.product_name = product_name
        self.qty_sold = qty_sold
        self.amount = amount
        self.product_id = product_id
        self.category = category


sale_request_parser = RequestParser(bundle_errors=True)
sale_request_parser.add_argument("sale_id", type=int, required=True, help="Please enter a valid integer for sale_id.")
sale_request_parser.add_argument("product_name", type=str, required=True, help="Product_name has to be a valid string")
sale_request_parser.add_argument("qty_sold", type=int, required=True, help="Please enter a valid integer for qty_sold")
sale_request_parser.add_argument("amount", type=int, required=True, help="Please enter a valid integer for amount")
sale_request_parser.add_argument("product_id", type=int, required=True, help="Please enter a valid integer for product_id")
sale_request_parser.add_argument("category", type=str, required=True, help="Category has to be a val  id string")