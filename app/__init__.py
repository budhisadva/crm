import os
from flask import Flask
# from werkzeug.middleware.proxy_fix import ProxyFix
# import json

def create_app():
    app = Flask(__name__)
    # config = json.load(open('/etc/crm/config.json'))
    app.config.from_mapping(
        SECRET_KEY = os.environ.get('SECRET_KEY'),
        DATABASE_HOST = os.environ.get('FLASK_DATABASE_HOST'),
        DATABASE_PASSWORD = os.environ.get('FLASK_DATABASE_PASSWORD'),
        DATABASE_USER = os.environ.get('FLASK_DATABASE_USER'),
        DATABASE = os.environ.get('FLASK_DATABASE'),
    )
    # app.wsgi_app = ProxyFix(
    #     app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
    # )
    from app.database import db
    db.init_app(app)
    from . import Dashboard
    app.register_blueprint(Dashboard.bp)
    return app
