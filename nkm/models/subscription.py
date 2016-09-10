from nkm import db
from datetime import datetime

TIMELIMIT = 24 * 3600
TIMELIMIT = 60


class Subscription(db.Model):
    """Subscription Model Class"""
    __tablename__ = 'subscriptions'
    id = db.Column(db.Integer, primary_key=True)
    term = db.Column(db.String, nullable=False)
    last_fetched = db.Column(db.DateTime, default=None)

    user_id = db.Column(
        db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    users = db.relationship("User", backref="subscriptions")

    def fetch(self):
        """fetch the subscription"""
        if not self.last_fetched:
            return True
        td = datetime.now() - self.last_fetched
        if td.total_seconds() > TIMELIMIT:
            return True
        else:
            return False
