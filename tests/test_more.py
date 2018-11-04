import unittest
import warnings
warnings.filterwarnings("ignore")
import pytest
import json
from storeapp import create_app
from storeapp.views.products_view import products
from storeapp.models.products_model import Product
from storeapp.views.sales_view import sales
from storeapp.models.sales_model import sale

app = create_app()
class TestFlaskMore(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_product_class(self):
        myclass = Product()
        self.assertIsInstance(myclass, Product)

    def test_sale_class(self):
        mySale = sale()
        self.assertIsInstance(mySale, sale)

    def test_run_app(self):
        self.assertIsNotNone(app)

    def tearDown(self):
        pass