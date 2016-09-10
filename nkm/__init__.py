import logging
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(os.environ.get('CONFIG', 'config.LocalConfig'))
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Logger
logger = logging.getLogger('nkm_logger')
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter(
    '%(relativeCreated)6d %(threadName)s %(message)s'
))
logger.addHandler(handler)
logger.setLevel(logging.INFO)


import views
