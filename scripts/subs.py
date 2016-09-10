import requests

root = 'http://nowknowmore.aavi.me'

r = requests.post(root + '/api/login', json={
    'email': 'string',
    'password': 'string'
})
at = r.json()['access_token']
print at

# add subscription
r = requests.post(root + '/api/subscriptions', json={
    'term': 'Politics'
}, headers={
    'Authorization': 'JWT %s' % at
})
print r.content
