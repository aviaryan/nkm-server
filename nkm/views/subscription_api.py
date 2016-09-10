import re
from datetime import datetime
from flask import request
from flask_restplus import Resource, fields
from nkm import logger
from nkm.views import api
from nkm.helpers.helpers import save_to_db, delete_from_db, identity, jwt_auth
from nkm.models.subscription import Subscription as SubscriptionModel
from nkm.models.article import Article as ArticleModel
from nkm.helpers.feeds import get_feeds
from article_api import ArticleDAO


SUBSCRIPTION_ARTICLE = api.model('SubscriptionArticle', {
    'id': fields.Integer(required=True),
    'link': fields.String(),
    'title': fields.String(),
    'text': fields.String(),
    'image': fields.String()
})

SUBSCRIPTION = api.model('Subscription', {
    'id': fields.Integer(required=True),
    'term': fields.String(required=True),
    'last_fetched': fields.DateTime()
})

SUBSCRIPTION_POST = api.clone('SubscriptionPost', SUBSCRIPTION)
del SUBSCRIPTION_POST['id']
del SUBSCRIPTION_POST['last_fetched']

SUBSCRIPTION_FULL = api.clone('SubscriptionFull', SUBSCRIPTION, {
    'articles': fields.List(fields.Nested(SUBSCRIPTION_ARTICLE))
})


class SubscriptionDAO():
    def get(self, sub_id):
        return SubscriptionModel.query.get(sub_id)

    def get_full(self, sub_id):
        sub = SubscriptionModel.query.get(sub_id)
        if not sub.fetch():
            return self.get_subs_image(sub)
        # delete old
        ArticleModel.query.filter_by(subscription_id=sub_id).delete()
        # re-fetch
        links = get_feeds(sub.term)
        for link in links:
            logger.info('Downloading %d' % len(links))
            ArticleDAOInstance.create(link, sub_id)
        # update LAT
        sub.last_fetched = datetime.now()
        save_to_db(sub)
        # return
        subs = SubscriptionModel.query.get(sub_id)
        return self.get_subs_image(subs)

    def get_subs_image(self, subs):
        if request.args.get('image') != 'none':
            return subs
        for article in subs.articles:
            article.text = re.sub(r'<img.*?/?\s*?>', '', article.text)
        return subs

    def create(self, data):
        sup = SubscriptionModel()
        sup.term = data['term']
        sup.last_fetched = None
        sup.user_id = identity().id
        if not save_to_db(sup):
            return 'Problem occured', 400
        return sup

    def list(self):
        return SubscriptionModel.query.filter_by(user_id=identity().id).all()

    def delete(self, sub_id):
        item = SubscriptionModel.query.get(sub_id)
        if delete_from_db(item):
            return item
        else:
            return 'Problem occured', 400


DAO = SubscriptionDAO()
ArticleDAOInstance = ArticleDAO()


@api.route('/subscriptions/<int:sub_id>')
class Subscription(Resource):
    @api.doc('get_subscription')
    @api.marshal_with(SUBSCRIPTION_FULL)
    def get(self, sub_id):
        """Fetch a subscription given its id"""
        return DAO.get_full(sub_id)

    @api.doc('delete_subscription')
    @api.marshal_with(SUBSCRIPTION)
    def delete(self, sub_id):
        """Delete a subscription given its id"""
        return DAO.delete(sub_id)


@api.route('/subscriptions')
class SubscriptionList(Resource):
    @api.doc('create_subscription')
    @api.marshal_with(SUBSCRIPTION)
    @api.expect(SUBSCRIPTION_POST)
    def post(self):
        """Create a subscription"""
        jwt_auth()
        return DAO.create(self.api.payload)

    @api.doc('get_subscription_list')
    @api.marshal_list_with(SUBSCRIPTION)
    def get(self):
        """List all subscriptions"""
        jwt_auth()
        return DAO.list()
