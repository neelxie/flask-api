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

    def test_app_exists(self):
        self.assertFalse(app is None)
     
    #Testing the get_product_by_id function with an integer
    def test_get_product_by_id(self):
        self.assertIsInstance(get_product_by_id(1), dict)

    def test_products_are_contained_in_list(self):
        self.assertIsInstance(products, list)

    def test_products_in_list_are_dict(self):
        product = products[0]
        self.assertIsInstance(product, dict)

    #Testing the get_sale_by_id function with an integer
    def test_get_sale_by_id(self):
        self.assertIsInstance(get_sale_by_id(1), dict)

    def test_sales_are_contained_in_list(self):
        self.assertIsInstance(sales, list)

    def test_sales_in_list_are_dict(self):
        sale = sales[0]
        self.assertIsInstance(sale, dict)



    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()