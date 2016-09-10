import logging
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt import JWT
from datetime import timedelta

app = Flask(__name__)
app.config.from_object(os.environ.get('CONFIG', 'config.LocalConfig'))
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# JWT
from helpers.jwt import jwt_authenticate, jwt_identity

app.config['JWT_AUTH_USERNAME_KEY'] = 'email'
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=24*60*60)
app.config['JWT_AUTH_URL_RULE'] = None
jwt = JWT(app, jwt_authenticate, jwt_identity)

# Logger
logger = logging.getLogger('nkm_logger')
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter(
    '%(relativeCreated)6d %(threadName)s %(message)s'
))
logger.addHandler(handler)
logger.setLevel(logging.INFO)


import views
