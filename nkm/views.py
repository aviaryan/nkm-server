from nkm import logger, app
# from flask import jsonify, request, render_template, url_for, make_response, Markup


@app.route('/')
def home():
    logger.info('Hell is this')
    return 'Hello America'
