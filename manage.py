# -*- coding: utf-8 -*-

"""
@Time        : 2020/12/20
@Author      : Administrator
@File        : manage.py
@Description : 
"""

from app import create_app

def make_shell_context():
    return dict(app=app,name='anan',age=10)

if __name__ == '__main__':
    # app=create_app()
    # host='0.0.0.0'其中0表示任意，这个IP则表示我的IP地址在共享时可以和任意一个IP地址绑定在一起
    # app.run()
    from flask_script import Manager, Shell

    app=create_app()
    manager=Manager(app)

    # 初始化 Flask-Script、Flask-Migrate和为Python shell定义的上下文
    manager.add_command('shell',Shell(make_context=make_shell_context))

    manager.run()