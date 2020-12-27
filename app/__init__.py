# -*- coding: utf-8 -*-

"""
@Time        : 2020/12/20
@Author      : Administrator
@File        : __init__.py
@Description : 
"""

"""
安装包, 在pycharm 中可以安装 
1）Flask-Bootstrap
2) Flask-Mail
3) Flask_Sqlalchemy
"""

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Message, Mail
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from config import config
from app.auth import auth
from app.todo import todo


bootstrap = Bootstrap()
db = SQLAlchemy()
mail = Mail()

# 设置login_manager
login_manager = LoginManager()
# session_protection 属性提供不同的安全等级防止用户会话遭篡改。
login_manager.session_protection = 'strong'
# login_view 属性设置登录页面的端点。
login_manager.login_view = 'auth.login'


def create_app(config_name='development'):
    """
    默认创建开发环境的app实例
    """
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    # 导入配置信息
    config[config_name].init_app(app)
    # 初始化app
    bootstrap.init_app(app)
    db.init_app(app)
    mail.init_app(app)

    # .......
    # 用户认证新加扩展,将第三方插件和app关联起来
    login_manager.init_app(app)
    # ........

    # 注册蓝图，将蓝图实例与app关联起来 : 验证蓝图
    app.register_blueprint(auth, url_prefix='/auth')

    # 注册蓝图，将蓝图实例与app关联起来 ： 任务蓝图
    app.register_blueprint(todo, url_prefix='/todo')

    return app
