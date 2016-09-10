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

    def test_add_other_user(self):
        """test adding sub in other user than 1"""
        self.register_user()
        at = self.get_access_token()
        self.register_user(email='test2@gmail.com')
        at2 = self.get_access_token(email='test2@gmail.com')
        # set sub 1
        resp = self.post_request('/api/subscriptions', data={
            'term': 'indian politics'
        }, at=at)
        self.assertIn('politics', resp.data)
        # set sub 2
        resp = self.post_request('/api/subscriptions', data={
            'term': 'vegetables'
        }, at=at2)
        self.assertIn('vegetables', resp.data)
        # get at 2
        resp = self.app.get('/api/subscriptions', headers={
            'Authorization': 'JWT %s' % at2
        })
        self.assertNotIn('politics', resp.data)
        self.assertIn('vegetable', resp.data)

    def test_no_jwt(self):
        """test default adding going to user 1"""
        self.register_user()
        resp = self.post_request('/api/subscriptions', data={
            'term': 'indian politics'
        })
        self.assertIn('politics', resp.data)
        resp = self.app.get('/api/subscriptions')
        self.assertIn('politics', resp.data)
        # test with at
        at = self.get_access_token()
        resp = self.app.get('/api/subscriptions', headers={
            'Authorization': 'JWT %s' % at
        })
        self.assertIn('politics', resp.data)
