from nkm import logger, app
from nkm.models.user import User


@app.route('/')
def home():
    logger.info('Hell is this')
    return 'Hello America'
