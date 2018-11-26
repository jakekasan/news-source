import os


class BaseConfig(object):
    SECRET = os.getenv('SECRET')

class DevelopmentConfig(BaseConfig):
    SQLITE_URI = os.getenv("DATABASE_URL")

class TestingConfig(BaseConfig):
    SQLITE_URI = "./tests/test.db"

app_config = {
    "development":DevelopmentConfig,
    "testing":TestingConfig
}