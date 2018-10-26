import unittest
import warnings
warnings.filterwarnings("ignore")
import pytest
import json
from storeapp import create_app
from storeapp.views.products_view import get_product_by_id
from storeapp.views.sales_view import get_sale_by_id
from storeapp.views.products_view import products
from storeapp.views.sales_view import sales


app = create_app()
class TestModelsAndViews(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_home_data(self):
        with self.app as c:
            resp = c.get('http://127.0.0.1:5000/api/v1/')
            print(resp)
            new_str = '"Store-Manager app by Sekidde Derrick"\n'
            self.assertEqual(resp.data.decode("utf-8"), new_str)
     
    #Testing the get_product_by_id function with an integer
    def test_get_product_by_id(self):
        self.assertIsInstance(get_product_by_id(1), dict)


    def test_get_sale_by_id(self):
        self.assertIsInstance(get_sale_by_id(1), dict)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()