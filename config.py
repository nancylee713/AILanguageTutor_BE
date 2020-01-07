import os

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    UNSPLASH_ACCESS_KEY = os.environ['UNSPLASH_ACCESS_KEY']
    DATABASE_URL = "postgresql://localhost/language_learner_dev"


class ProductionConfig(Config):
    DEBUG = False

class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    DATABASE_URL = os.environ['DATABASE_URL'] # heroku-staging db

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class TestingConfig(Config):
    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False
