import sqlite3
import unittest
import os
import json
from app import create_app, db
from instance import config



class MainTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.test_data = {'date','01-01-2012'}

        with self.app.app_context():
            db.create_all()

    def test_get_db_local(self):
        """
        test a get request for data which is in DB
        """
        pass

    def test_get_db_not_local(self):
        """
        test a get request for data which is not stored in DB
        """
        pass
