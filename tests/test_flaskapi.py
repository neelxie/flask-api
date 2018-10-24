import unittest
import warnings
warnings.filterwarnings("ignore")
import json
import pytest
from storeapp import create_app
from copy import deepcopy
from storeapp.products import products
from storeapp.sales import sales


app = create_app()
class TestFlaskApi(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    """ Test product creation endpoint """

    def test_api_product_creation(self):
        with self.app as c:
            resp = c.post('http://127.0.0.1:5000/api/v1/Products', data=json.dumps(
                {"id": 3, "name": "cups", "qty": 326,"Min-Stock": 150, "price": 29000, "Units": 38, "category": "kitchen-ware"}), content_type='application/json')
            self.assertEqual(resp.status_code, 201)
            # self.assertEqual(data['id'], 3)

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

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()