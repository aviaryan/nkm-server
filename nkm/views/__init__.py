from flask_restplus import Api
from nkm import app
from nkm.models.user import User


api = Api(app, prefix='/api', doc='/api')


import public_views
import user_api
import login_api
import subscription_api
import article_api
