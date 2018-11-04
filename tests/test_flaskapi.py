import unittest
import warnings
warnings.filterwarnings("ignore")
import pytest
import json
from storeapp import create_app
from storeapp.views.products_view import products, ProductList
from storeapp.views.sales_view import sales


app = create_app()
jaja = ProductList()
class TestFlaskApi(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_index_url(self):
        """ Testing the index file."""
        with self.app as c:
            resp = c.get('http://127.0.0.1:5000/api/v1/')
            self.assertEqual(resp.status_code, 200)

    def test_home_data(self):
        """ Testing the message in the index file."""
        with self.app as c:
            resp = c.get('http://127.0.0.1:5000/api/v1/')
            new_str = '"Store-Manager app by Sekidde Derrick"\n'
            self.assertEqual(resp.data.decode("utf-8"), new_str)

    """ Test product creation endpoint """

    def test_api_product_creation(self):
        with self.app as c:
            resp = c.post('http://127.0.0.1:5000/api/v1/Products', data=json.dumps(
                {"name": "cups", "qty": 326, "min_stock": 150, "price": 29000, "units": 38, "category": "kitchen-ware"}), content_type='application/json')
            self.assertEqual(resp.status_code, 201)

    def test_authenticate_product_creation(self):
        with self.app as c:
            resp = c.post('http://127.0.0.1:5000/api/v1/Products', data=json.dumps(
                {"name": "cups", "qty": 326, "min_stock": 150, "price": " ", "units": 38, "category": "kitchen-ware"}), content_type='application/json')
            self.assertEqual(resp.data, b'{"msg": "product price must be a number."}\n')

    def test_authenticate_product_name(self):
        with self.app as c:
            resp = c.post('http://127.0.0.1:5000/api/v1/Products', data=json.dumps(
                {"name": 45, "qty": 326, "min_stock": 150, "price": 2565, "units": 38, "category": "kitchen-ware"}), content_type='application/json')
            self.assertEqual(resp.data, b'{"msg": "product name must be a string."}\n')

    def test_authenticate_product_name_missing(self):
        with self.app as c:
            resp = c.post('http://127.0.0.1:5000/api/v1/Products', data=json.dumps(
                {"name": None, "qty": 326, "min_stock": 150, "price": 29235, "units": 38, "category": "kitchen-ware"}), content_type='application/json')
            self.assertEqual(resp.data, b'{"msg": "product name missing."}\n')

    def test_authenticate_product_name_space(self):
        with self.app as c:
            resp = c.post('http://127.0.0.1:5000/api/v1/Products', data=json.dumps(
                {"name": " ", "qty": 326, "min_stock": 150, "price": 5445, "units": 38, "category": "kitchen-ware"}), content_type='application/json')
            self.assertEqual(resp.data, b'{"msg": "product name is missing"}\n')

    def test_authenticate_product_name_letters(self):
        with self.app as c:
            resp = c.post('http://127.0.0.1:5000/api/v1/Products', data=json.dumps(
                {"name": "645", "qty": 326, "min_stock": 150, "price": 4550, "units": 38, "category": "kitchen-ware"}), content_type='application/json')
            self.assertEqual(resp.data, b'{"msg": "product name should only be letters"}\n')

    def test_authenticate_product_quantity(self):
        with self.app as c:
            resp = c.post('http://127.0.0.1:5000/api/v1/Products', data=json.dumps(
                {"name": "soda", "qty": None, "min_stock": 150, "price": 4523, "units": 38, "category": "kitchen-ware"}), content_type='application/json')
            self.assertEqual(resp.data, b'{"msg": "product quantity missing."}\n')

    def test_authenticate_product_quantity_number(self):
        with self.app as c:
            resp = c.post('http://127.0.0.1:5000/api/v1/Products', data=json.dumps(
                {"name": "soda", "qty": "bnn", "min_stock": 150, "price": 5442, "units": 38, "category": "kitchen-ware"}), content_type='application/json')
            self.assertEqual(resp.data, b'{"msg": "product quantity must be a number."}\n')

    def test_authenticate_product_minstock(self):
        with self.app as c:
            resp = c.post('http://127.0.0.1:5000/api/v1/Products', data=json.dumps(
                {"name": "soda", "qty": 326, "min_stock": None, "price": " ", "units": 38, "category": "kitchen-ware"}), content_type='application/json')
            self.assertEqual(resp.data, b'{"msg": "product min_stock missing."}\n')

    def test_authenticate_product_price(self):
        with self.app as c:
            resp = c.post('http://127.0.0.1:5000/api/v1/Products', data=json.dumps(
                {"name": "soda", "qty": 326, "min_stock": 150, "price": None, "units": 38, "category": "kitchen-ware"}), content_type='application/json')
            self.assertEqual(resp.data, b'{"msg": "product price missing."}\n')

    def test_authenticate_product_units(self):
        with self.app as c:
            resp = c.post('http://127.0.0.1:5000/api/v1/Products', data=json.dumps(
                {"name": "mputa", "qty": 326, "min_stock": 150, "price": 452, "units": None, "category": "kitchen-ware"}), content_type='application/json')
            self.assertEqual(resp.data, b'{"msg": "product units missing."}\n')

    def test_authenticate_product_minstock_number(self):
        with self.app as c:
            resp = c.post('http://127.0.0.1:5000/api/v1/Products', data=json.dumps(
                {"name": "fene", "qty": 326, "min_stock": "ggh", "price": 456, "units": 38, "category": "kitchen-ware"}), content_type='application/json')
            self.assertEqual(resp.data, b'{"msg": "product min_stock must be a number."}\n')

    def test_authenticate_product_units_number(self):
        with self.app as c:
            resp = c.post('http://127.0.0.1:5000/api/v1/Products', data=json.dumps(
                {"name": "gweke", "qty": 326, "min_stock": 150, "price": 4522, "units": "gdhs", "category": "kitchen-ware"}), content_type='application/json')
            self.assertEqual(resp.data, b'{"msg": "product units must be a number."}\n')

    def test_authenticate_product_category_missing(self):
        with self.app as c:
            resp = c.post('http://127.0.0.1:5000/api/v1/Products', data=json.dumps(
                {"name": "fene", "qty": 326, "min_stock": 150, "price": 29235, "units": 38, "category": None}), content_type='application/json')
            self.assertEqual(resp.data, b'{"msg": "product category missing."}\n')

    def test_authenticate_product_category(self):
        with self.app as c:
            resp = c.post('http://127.0.0.1:5000/api/v1/Products', data=json.dumps(
                {"name": "fene", "qty": 326, "min_stock": 150, "price": 29235, "units": 38, "category": 4552}), content_type='application/json')
            self.assertEqual(resp.data, b'{"msg": "product category must be a string."}\n')

    """ Test get all products endpoint """

    def test_get_all_products(self):
        with self.app as c:
            response = c.get('http://127.0.0.1:5000/api/v1/Products')
            self.assertEqual(response.status_code, 200)

    def test_get_a_product_by_id(self):
        with self.app as c:
            response = c.get('http://127.0.0.1:5000/api/v1/Products/1')
            self.assertEqual(response.status_code, 200)

    def test_get_product_by_wrong_id(self):
        with self.app as c:
            response = c.get('http://127.0.0.1:5000/api/v1/Products/9')
            self.assertEqual(response.data, b'{"error": "product not found"}\n')

    def test_sales_record_creation(self):
        with self.app as c:
            response = c.post('http://127.0.0.1:5000/api/v1/Sales', data=json.dumps(
                {'sale_id': 3, 'name': 'briefs','qty_sold': 2,'amount': 4500, 'product_id': 38,'category': 'clothes'}), content_type='application/json')
            self.assertEqual(response.status_code, 201)

    def test_get_sale_record_given_bad_id(self):
        with self.app as c:
            response = c.get('http://127.0.0.1:5000/api/v1/Sales/9')
            self.assertEqual(response.data, b'{"error": "sale not found"}\n')

    def test_retrieve_all_sale_records(self):
        with self.app as c:
            response = c.get('http://127.0.0.1:5000/api/v1/Sales')
            self.assertEqual(response.status_code, 200)

    def test_get_sale_record_given_an_id(self):
        with self.app as c:
            response = c.get('http://127.0.0.1:5000/api/v1/Sales/2')
            self.assertEqual(response.status_code, 200)

    def test_nonexistant_product(self):
        with self.app as c:
            response = c.get('http://127.0.0.1:5000/api/v1/Products/<product_id>')
            self.assertEqual(response.status_code, 404)

    def test_nonexistant_sale(self):
        with self.app as c:
            response = c.get('http://127.0.0.1:5000/api/v1/Products/<sale_id>')
            self.assertEqual(response.status_code, 404)

    def tearDown(self):
        pass