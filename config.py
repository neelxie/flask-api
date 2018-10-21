import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    SECRET_KEY = 'STeal-THis-ANd-I-WIll-KEel-YOu-ANd-EVeryone-YOu-KNow'
    CRSF_ENABLED = True

class ProductionConfig(Config):
    DEBUG = False

class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    
class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

config = TestingConfig