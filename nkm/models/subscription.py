from nkm import db


class Subscription(db.Model):
    """Subscription Model Class"""
    __tablename__ = 'subscriptions'
    id = db.Column(db.Integer, primary_key=True)
    term = db.Column(db.String, nullable=False)

    user_id = db.Column(
        db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    users = db.relationship("User", backref="session_type")
