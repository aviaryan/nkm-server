from tests import NKMTestCase


class TestUser(NKMTestCase):
    """tests the user features"""
    def test_account_create(self):
        resp = self.post_request('/api/users', data={
            'email': 'test@gmail.com',
            'password': 'test'
        })
        self.assertEqual(resp.status_code, 200)
        self.assertIn('test', resp.data)

    def test_jwt_login(self):
        pass
