from nkm.models.article import Article as ArticleModel
from nkm.helpers.parser import get_page_html, extract_article_info
from nkm.helpers.helpers import save_to_db


class ArticleDAO():
    def create(self, link, sub_id):
        html = get_page_html(link)
        article_info = extract_article_info(html)
        article = ArticleModel()
        article.link = link
        article.title = article_info['title']
        article.text = article_info['content']
        article.subscription_id = sub_id
        if save_to_db(article):
            return article
        else:
            return 'Some Error Occured', 400
