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

    def register_user(self, email='test@gmail.com'):
        """
        registers a user
        """
        self.post_request('/api/users', data={
            'email': email,
            'full_name': 'Mi Hawk',
            'password': 'test'
        })

    def post_request(self, path, data, at=None):
        """
        send a post request to a url
        """
        hdrs = {'content-type': 'application/json'}
        if at:
            hdrs['Authorization'] = 'JWT %s' % at
        return self.app.post(
            path,
            data=json.dumps(data),
            headers=hdrs
        )

    def get_access_token(self, email='test@gmail.com'):
        """
        gets access token
        """
        resp = self.post_request('/api/login', data={
            'email': email,
            'password': 'test'
        })
        return json.loads(resp.data)['access_token']
