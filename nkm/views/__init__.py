from flask_restplus import Api
from nkm import logger, app
from nkm.models.user import User
from nkm.helpers.parser import get_page_html, extract_article_info


api = Api(app, doc='/api')


@app.route('/')
def home():
    logger.info('Hell is this')
    z = get_page_html('http://aviaryan.in/blog/gsoc/docker-compose-starting.html')
    return extract_article_info(z)['content']


import user_api
