from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    # 注册蓝图
    from apps.admin import admin
    from apps.front import front
    from apps.home import home
    app.register_blueprint(admin)
    app.register_blueprint(front)
    app.register_blueprint(home)
    return app