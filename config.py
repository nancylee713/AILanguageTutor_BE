import os

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    UNSPLASH_ACCESS_KEY = os.environ['UNSPLASH_ACCESS_KEY']
    SQLALCHEMY_DATABASE_URI = "postgresql://localhost/language_learner_dev"


class ProductionConfig(Config):
    DEBUG = False

class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL'] # heroku-staging db
    PRESERVE_CONTEXT_ON_EXCEPTION = False

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class TestingConfig(Config):
    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False
