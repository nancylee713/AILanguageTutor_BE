import os

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    UNSPLASH_ACCESS_KEY = os.environ['UNSPLASH_ACCESS_KEY']
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class TestingConfig(Config):
    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False
