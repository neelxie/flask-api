import unittest
import json
#import app
from storeapp.products import Products
from storeapp.sales import Sales

BASE_URL = 'http://127.0.0.1:5000/storemanager/api/v1//Sales'

class TestFlaskApi(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.pdts_db = Products()

    """ Test product creation endpoint """

    def test_api_product_creation(self):
        with self.app as c:
            response = c.post('http://127.0.0.1:5000/storemanager/api/v1//products')
            self.assertEqual(response.status_code, 400)
            resp = c.post('http://127.0.0.1:5000/storemanager/api/v1//products', data=json.dumps(
                {'name': 'pixel', 'category': 'electronic', 'price': 40}), content_type='application/json')
            self.assertEqual(resp.status_code, 201)

    """ Test get all products endpoint """

    def test_get_all_products(self):
        with self.app as c:
            response = c.get('http://127.0.0.1:5000/storemanager/api/v1//Products')
            self.assertEqual(response.status_code, 200)

    def test_get_a_product_by_id(self):
        with self.app as c:
            response = c.get('http://127.0.0.1:5000/storemanager/api/v1//Products/soaks')
            self.assertEqual(response.status_code, 400)
            resp = c.post('http://127.0.0.1:5000/storemanager/api/v1//products', data=json.dumps(
                {'name': 'pixel', 'category': 'electronic', 'price': 40}), content_type='application/json')
            responseAfterPdtCreation = c.get('http://127.0.0.1:5000/storemanager/api/v1//Products/1')
            print(responseAfterPdtCreation)
            self.assertIsNotNone(responseAfterPdtCreation)
            expected = json.loads(responseAfterPdtCreation.data)
            self.assertEqual('pixel', expected['name'])

    def test_sales_record_creation(self):
        with self.app as c:
            response = c.post('http://127.0.0.1:5000/storemanager/api/v1//Sales', data=json.dumps(
                {'sale_id': 3, 'name': 'briefs','qty_sold': 2,'amount': 4500, 'product_id': 38,'category': 'clothes'}), content_type='application/json')
            self.assertEqual(response.status_code, 201)

    def test_retrieve_all_sale_records(self):
        with self.app as c:
            response = c.get('http://127.0.0.1:5000/storemanager/api/v1//Sales')
            self.assertEqual(response.status_code, 200)

    def test_get_sale_record_given_an_id(self):
        with self.app as c:
            response = c.get('http://127.0.0.1:5000/storemanager/api/v1//Sale/2')
            self.assertEqual(response.status_code, 400)

    def tearDown(self):
        app.items = self.backup_items

if __name__ == '__main__':
    unittest.main()