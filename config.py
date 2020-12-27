"""
存储配置;
"""
import os

# 获取当前项目的绝对路径;
basedir = os.path.abspath(os.path.dirname(__file__))
#print(basedir)

class Config:
    """
    所有配置环境的基类，即不管是开发环境还是测试环境，配置相同的
    都写在Config里面，包含通用配置，称为配置环境的基类
    """
    # 加密key值，一般在闪现信息时用FLASK_APP
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'westos secret key'
    # 数据库自动提交
    # 尤其在涉及（flask-WTF）登陆页面提交敏感信息时，一定要设置密钥
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # 跟踪数据库修改，
    # 是否自动提交
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # 是否追踪修改，从Flask-SQLALchemy文档中查看
    FLASK_MAIL_SUBJECT_PREFIX = '安安的ToDolist'
    FLASK_MAIL_SENDER = '792910452@qq.com'


    @staticmethod
    def init_app(app):
        """
        初始化app,后续用来添加第三方插件
        """
        pass


class DevelopmentConfig(Config):
    """
    开发环境配置
    """
    DEBUG=True
    # 启用调试支持，服务器会在代码修改后自动载入，并在发生错误时提供一个相当有用的调试器
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 587
    MAIL_USE_TLS=True
    # 这里的os.environ.get()指从系统的环境中获取（）,environ是与Linux配套的
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or '792910452'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or '密码'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
    # 开发环境下的数据存放在当前文件下的data-dev的sqlite中


class TestingConfig(Config):
    """
    测试环境的配置信息
    """
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    """
    生产环境的配置信息
    """
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')


# 为每一个配置环境起一个名字
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
    # 默认是在开发环境中
}
