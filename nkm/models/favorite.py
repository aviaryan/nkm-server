from nkm import db


class FavArticle(db.Model):
    """Fav Article Model Class"""
    __tablename__ = 'fav_articles'
    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String)
    title = db.Column(db.String)
    text = db.Column(db.String)
    image = db.Column(db.String)
    website = db.Column(db.String)

    user_id = db.Column(
        db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    users = db.relationship("User", backref="fav_articles")
