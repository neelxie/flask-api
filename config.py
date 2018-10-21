import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    SECRET_KEY = 'STeal-THis-ANd-I-WIll-KEel-YOu-ANd-EVeryone-YOu-KNow'
    CRSF_ENABLED = True

class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    
class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class ProductionConfig(Config):
    """Configurations for Production"""
    pass


app_config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig
}
