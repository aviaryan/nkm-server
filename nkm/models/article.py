from nkm import db


class Article(db.Model):
    """Article Model Class"""
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String)
    title = db.Column(db.String)
    text = db.Column(db.String)
    image = db.Column(db.String)

    subscription_id = db.Column(
        db.Integer, db.ForeignKey('subscriptions.id', ondelete='CASCADE'))
    subscriptions = db.relationship("Subscription", backref="articles")
