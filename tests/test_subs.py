from tests import NKMTestCase


class TestSubs(NKMTestCase):
    """tests the subscription"""
    def test_add_sub(self):
        self.register_user()
        at = self.get_access_token()
        resp = self.post_request('/api/subscriptions', data={
            'term': 'indian politics'
        }, at=at)
        self.assertIn('politics', resp.data)

    def test_get_sub(self):
        self.test_add_sub()
        resp = self.app.get('/api/subscriptions/1')
        self.assertTrue(len(resp.data) > 500)
        self.assertIn('politics', resp.data)
