import json
from flask.ext.restplus import Resource, fields
from flask_jwt import JWTError
from nkm.views import api

LOGIN = api.model('Login', {
    'email': fields.String(required=True),
    'password': fields.String(required=True)
})

TOKEN = api.model('Token', {
    'access_token': fields.String
})


@api.route('/api/login')
class Login(Resource):
    @api.doc('get_token')
    @api.expect(LOGIN, validate=True)
    @api.marshal_with(TOKEN)
    def post(self):
        from .. import jwt
        try:
            response = jwt.auth_request_callback()
            return json.loads(response.data)
        except JWTError as e:
            return e.error, 400
