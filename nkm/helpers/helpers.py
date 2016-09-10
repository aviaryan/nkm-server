import traceback
from nkm import db


def save_to_db(item):
    """Save a model to database"""
    try:
        db.session.add(item)
        db.session.commit()
        return True
    except Exception:
        traceback.print_exc()
        db.session.rollback()
        return False


def delete_from_db(item):
    """Delete a model from database"""
    try:
        db.session.delete(item)
        db.session.commit()
        return True
    except Exception:
        traceback.print_exc()
        db.session.rollback()
        return False
