# -*- coding: utf-8 -*-

"""
@Time        : 2020/12/20
@Author      : Administrator
@File        : models.py
@Description : 
"""

from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager

"""
添加UserMixin后在终端中执行python manage.py shell
在交互环境下查看user具有哪些属性
users=User.query.all()
users
user=users[0]
dir(user) 查看用户具有哪些属性和方法
user.username  查看用户的username属性信息
这些方法在写逻辑代码时使用
print(user.is_active)
"""


class User(UserMixin, db.Model):

    """
    用户信息

    因为继承了UserMixin类,自动继承里面的属性和方法
    Flask-Login提供了一个UserMixin类，包含常用方法的默认实现，且能满足大多数需求
       1）is_authenticated 用户是否已经登录
       2）is_active 是否允许用户登录？False代表用户禁用
       3）is_anonymous 是否匿名用户
       4）get_id() 返回用户的唯一标识符
    """
    __tablename__ = 'users'  # 自定义数据表的表名
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=True)
    email = db.Column(db.String(50))
    phone = db.Column(db.String(20))

    # 外键写在多的一端，外键关联的是roles表中的id列
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        # generate_password_hash(password,method=pbkd2:sha1,salt_length=8):密码加密的散列值，为密码进行哈希加密
        self.password_hash = generate_password_hash(password)

    def verity_password(self, password):
        # check_password_hash(hash,password):密码散列值和用户输入的密码是否一致
        return check_password_hash(self.password_hash, password)

    def __repr__(self): return '<User % r>' % self.username

# 加载用户的回调函数；如果能找到用户，返回用户对象；否则返回None
# 当有用户登录时，通过查询用户id，返回此用户id对应的用户信息

# login回调函数的作用：
# 注册回调函数 当没有session_id时，通过装饰器指定的函数来读取用户到session中
# 达到前端可通过current_user去获取当前登录的用户

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Role(db.Model):
    __tablename__='roles'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(100),unique=True,nullable=False)
    # 做了两件事：1）Role添加属性users 2）User添加属性role
    users=db.relationship('User',backref='role')

    def __repr__(self):
        return '<Role:%s>'%(self.name)