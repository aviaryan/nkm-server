import json
from nkm import logger, app
from nkm.helpers.parser import get_page_html, extract_article_info
from nkm.helpers.feeds import get_feeds


@app.route('/')
def home():
    logger.info('Hell is this')
    # z = get_page_html(
    #     'http://aviaryan.in/blog/gsoc/docker-compose-starting.html'
    # )
    # return extract_article_info(z)['content']
    return json.dumps(get_feeds('Artifical Intelligence'))
