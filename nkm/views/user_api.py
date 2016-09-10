from flask_restplus import Resource, fields
from nkm.views import api
from nkm.helpers.helpers import save_to_db
from nkm.models.user import User as UserModel


USER = api.model('User', {
    'id': fields.Integer(required=True),
    'email': fields.String(required=True),
    'full_name': fields.String()
})

USER_POST = api.clone('UserPost', USER, {
    'password': fields.String()
})
del USER_POST['id']


class UserDAO():
    def get(self, user_id):
        return UserModel.query.get(user_id)

    def create(self, data):
        user = UserModel()
        user.email = data['email']
        user.phash = user.hash_password(data['password'])
        user.full_name = data.get('full_name')
        if not save_to_db(user):
            return 'Email exists', 400
        return user


DAO = UserDAO()


@api.route('/users/<int:user_id>')
class User(Resource):
    @api.doc('get_user')
    @api.marshal_with(USER)
    def get(self, user_id):
        """Fetch a user given its id"""
        return DAO.get(user_id)


@api.route('/users')
class UserList(Resource):
    @api.doc('create_user')
    @api.marshal_with(USER)
    @api.expect(USER_POST)
    def post(self):
        """Create a user"""
        return DAO.create(self.api.payload)
