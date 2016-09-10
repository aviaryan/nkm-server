from nkm.models.user import User

# @jwt_required


def jwt_authenticate(email, password):
    user = User.query.filter_by(email=email).first()
    if user is None:
        return None
    auth_ok = (user.phash == user.hash_password(password))
    if auth_ok:
        return user
    else:
        return None


def jwt_identity(payload):
    return User.query.get(payload['identity'])
