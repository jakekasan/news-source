import os


class BaseConfig(object):
    SECRET = os.getenv('SECRET')

class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")

class TestingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "./tests/test.db"

app_config = {
    "development":DevelopmentConfig,
    "testing":TestingConfig
}