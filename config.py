import os

LOCAL_PSQLDB_URL = 'postgresql://project:project@localhost/nkm'


class Config(object):
    DEBUG = True
    CSRF_ENABLED = True
    SECRET_KEY = 'asdk23akdskdsaasd'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../database.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class LocalConfig(Config):
    SQLALCHEMY_DATABASE_URI = LOCAL_PSQLDB_URL


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', LOCAL_PSQLDB_URL)


class HerokuConfig(ProductionConfig):
    DEBUG = True


class OpenShiftConfig(ProductionConfig):
    SQLALCHEMY_DATABASE_URI = os.environ.get('OPENSHIFT_POSTGRESQL_DB_URL')


class SQLiteConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../database.sqlite3'
