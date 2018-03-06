from flask import current_app


def get_user(username):
    return current_app.mongo.db.user.find_one({'username': username})

