import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    db_connection = os.environ.get("DATABASE_URL")
    if db_connection.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI = db_connection.replace('postgres://', 'postgresql://')
    else:
        SQLALCHEMY_DATABASE_URI = db_connection


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
