from distutils.debug import DEBUG
import os

base_dir = os.path.abspath(os.path.dirname(__name__))

class DevelopmentConfig:
    DEBUG = True

class ProductionConfig:
    DEBUG = False

class TestingConfig:
    DEBUG = False
    TESTING = True