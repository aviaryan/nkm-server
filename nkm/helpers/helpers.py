import traceback
from nkm import db, logger
from flask_jwt import current_identity, jwt_required


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


def identity():
    try:
        id_ = current_identity.id
        return current_identity
    except Exception:
        logger.info('Current Id No')
        # logger.info(traceback.format_exc())
        from nkm.models.user import User
        return User.query.get(1)


def jwt_auth():
    try:
        jwt_auth_2()
    except Exception:
        logger.info('Jwt No')
        # logger.info(traceback.format_exc())


@jwt_required()
def jwt_auth_2():
    pass
