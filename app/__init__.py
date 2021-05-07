from flask  import Flask
from .extensions import mongo
from .domain.faq.controller import controller

def register_controllers(app:Flask):
    app.register_blueprint(controller)

def create_app(config_object= 'settings.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config_object)
    mongo.init_app(app)
    register_controllers(app)
    return app