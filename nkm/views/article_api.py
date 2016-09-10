from nkm.models.article import Article as ArticleModel
from nkm.models.favorite import FavArticle as FavArticleModel
from nkm.helpers.parser import get_page_html, extract_article_info
from nkm.helpers.helpers import save_to_db, delete_from_db
from flask_restplus import Resource, fields
from nkm.views import api


FAVORITE_ARTICLE = api.model('FavoriteArticle', {
    'id': fields.Integer(required=True),
    'link': fields.String(),
    'title': fields.String(),
    'text': fields.String(),
    'image': fields.String()
})


class ArticleDAO():
    def create(self, link, sub_id):
        html = get_page_html(link)
        article_info = extract_article_info(html)
        article = ArticleModel()
        article.link = link
        article.title = article_info['title']
        article.text = article_info['content']
        article.image = article_info['image']
        article.subscription_id = sub_id
        if save_to_db(article):
            return article
        else:
            return 'Some Error Occured', 400


class FavoriteArticleDAO():
    def create(self, article_id):
        article = ArticleModel.query.get(article_id)
        fav = FavArticleModel()
        fav.link = article.link
        fav.title = article.title
        fav.text = article.text
        fav.image = article.image
        fav.user_id = 1  # CHANGE
        if save_to_db(fav):
            return fav
        else:
            return 'Some Error Occured', 400

    def list(self):
        return FavArticleModel.query.filter_by(user_id=1).all()

    def delete(self, article_id):
        item = FavArticleModel.query.get(article_id)
        if delete_from_db(item):
            return item
        else:
            return 'Problem occured', 400


FavDAO = FavoriteArticleDAO()


@api.route('/articles/<int:article_id>/favorite')
class FavoriteArticle(Resource):
    @api.doc('set_fav_article')
    @api.marshal_with(FAVORITE_ARTICLE)
    def post(self, article_id):
        """Make an article favorite"""
        return FavDAO.create(article_id)

    @api.doc('delete_fav_article')
    @api.marshal_with(FAVORITE_ARTICLE)
    def delete(self, article_id):
        """Delete a fav article given its id"""
        return FavDAO.delete(article_id)


@api.route('/articles/favorites')
class FavoriteArticleList(Resource):
    @api.doc('get_fav_article_list')
    @api.marshal_list_with(FAVORITE_ARTICLE)
    def get(self):
        """List all fav articles"""
        return FavDAO.list()
