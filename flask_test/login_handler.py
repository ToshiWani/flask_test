from flask import current_app, flash
from flask_login import UserMixin
import flask_test.database_helper as db_helper

@current_app.login_manager.user_loader
def user_loader(username):
    return _get_user(username)


def authenticate(username, password):
    """
    Validates username and password
    :param username: string
    :param password: string
    :return: User
    """
    if _authenticate_ad(username, password):
        user = _get_user(username)

        if user is None:
            flash('Login error!', 'error')
            return None
        else:
            return _get_user(username)


def _authenticate_ad(username, password):
    """
    Authenticate through Active Directory
    :param username: string
    :param password: string
    :return: boolean
    """
    response = current_app.ldap3_login_manager.authenticate(username, password)
    return response.status.name == 'success'


def _get_user(username):
    """
    Get user by username
    :param username: string
    :return: User
    """
    user = db_helper.get_user(username)

    result = User(username)
    result.is_active = user['is_active']
    result.is_authenticated = True
    result.is_anonymous = False
    return result


class User(UserMixin):
    is_authenticated = False
    is_active = False
    is_anonymous = True
    username = ''
    display_name = ''

    def __init__(self, username):
        self.username = username

    def get_id(self):
        return self.username


