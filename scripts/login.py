import requests

root = 'http://nowknowmore.aavi.me'

r = requests.post(root + '/api/login', json={
    'email': 'string',
    'password': 'string'
})
print r.content
