import os

class DevelopmentConfig(object):
    SECRET = os.getenv('SECRET')
    SQLITE_URI = os.getenv("DATABASE_URL")

app_config = {
    "development":DevelopmentConfig
}