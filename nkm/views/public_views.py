# import json
from flask import render_template
from nkm import logger, app
# from nkm.helpers.parser import get_page_html, extract_article_info
# from nkm.helpers.feeds import get_feeds


@app.route('/')
def home():
    return render_template('/index.html')
