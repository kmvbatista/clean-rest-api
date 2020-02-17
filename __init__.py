from flask  import Flask
from extensions import mongo
from domain.user.controller import app_users

def create_app(config_object= 'settings.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config_object)
    mongo.init_app(app)
    app.register_blueprint(app_users)
    return app