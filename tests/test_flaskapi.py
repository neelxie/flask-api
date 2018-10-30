import unittest
import warnings
warnings.filterwarnings("ignore")
import pytest
import json
from storeapp import create_app
from storeapp.views.products_view import products
from storeapp.views.sales_view import sales


app = create_app()
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

    """ Test get all products endpoint """

    def test_get_all_products(self):
        with self.app as c:
            response = c.get('http://127.0.0.1:5000/api/v1/Products')
            self.assertEqual(response.status_code, 200)

    def test_get_a_product_by_id(self):
        with self.app as c:
            response = c.get('http://127.0.0.1:5000/api/v1/Products/1')
            self.assertEqual(response.status_code, 200)

    def test_sales_record_creation(self):
        with self.app as c:
            response = c.post('http://127.0.0.1:5000/api/v1/Sales', data=json.dumps(
                {'sale_id': 3, 'name': 'briefs','qty_sold': 2,'amount': 4500, 'product_id': 38,'category': 'clothes'}), content_type='application/json')
            self.assertEqual(response.status_code, 201)

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

if __name__ == '__main__':
    unittest.main()