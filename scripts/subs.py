import requests

root = 'http://nowknowmore.aavi.me'
# root = 'http://localhost:5000'

r = requests.post(root + '/api/login', json={
    'email': 'string3',
    'password': 'string'
})
at = r.json()['access_token']
print at

# get subscription
r = requests.get(root + '/api/subscriptions', headers={
    'Authorization': 'JWT %s' % at
})
print r.content

# add subscription
r = requests.post(root + '/api/subscriptions', json={
    'term': 'Politics China'
}, headers={
    'Authorization': 'JWT %s' % at
})
print r.content


# get single sub
# r = requests.get(root + '/api/subscriptions/17')
# print r.content
