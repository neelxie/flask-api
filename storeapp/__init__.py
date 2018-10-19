import os

from flask import Flask
from storeapp.products import Products
from storeapp.sales import Sales
from storeapp.users import Users

myapp = Flask(__name__)

from storeapp import routes