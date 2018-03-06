from flask import Flask
from flask_login import LoginManager
from flask_ldap3_login import LDAP3LoginManager
from flask_pymongo import PyMongo

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile(filename='application.cfg')

# Register Login
login_manager = LoginManager(app)
login_manager.login_view = 'test.login'

# Register LDAP
ldap_manager = LDAP3LoginManager(app)

# Register PyMango
app.mongo = PyMongo(app)


with app.app_context():
    # Register Blueprint
    from flask_test.blueprints.test.views import mod
    app.register_blueprint(mod)
