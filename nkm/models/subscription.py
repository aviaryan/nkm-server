from nkm import db
from datetime import datetime

TIMELIMIT = 24 * 3600


class Subscription(db.Model):
    """Subscription Model Class"""
    __tablename__ = 'subscriptions'
    id = db.Column(db.Integer, primary_key=True)
    term = db.Column(db.String, nullable=False)
    last_fetched = db.Column(db.DateTime)

    user_id = db.Column(
        db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    users = db.relationship("User", backref="session_type")

    def fetch(self):
        """fetch the subscription"""
        td = datetime.now() - self.last_fetched
        if td.total_seconds() > TIMELIMIT:
            return True
        else:
            return False
