import unittest
import os
import json
from nkm import app, db


class NKMTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../test.sqlite3'
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        os.unlink('test.sqlite3')

    def post_request(self, path, data):
        """
        send a post request to a url
        """
        return self.app.post(
            path,
            data=json.dumps(data),
            headers={'content-type': 'application/json'}
        )
