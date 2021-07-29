"""
# coding:utf-8
@Time    : 2021/07/27
@Author  : jiangwei
@mail    : qq804022023@gmail.com
@File    : __init__.py.py
@Desc    : __init__.py
@Software: PyCharm
"""
from flask import Flask
import click
from app.extensions import db, mg
from app.models import User, UserRole, Permission, MemberShip, RolePermission
from app.config import DevelopmentConfig
from app.view import sso


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    app.register_blueprint(sso)
    register_extensions(app)
    register_cmd(app)
    return app


def register_extensions(app: Flask):
    db.init_app(app)
    mg.init_app(app, db)


def register_cmd(app: Flask):
    @app.cli.command()
    def initdb():
        click.confirm('This operation will drop the database, do you want to continue?', abort=True)
        db.drop_all()
        db.create_all()
        click.echo('Database initialing success.')

    @app.cli.command()
    def addadmin():
        init_data()
        import re


def init_data():
    try:
        p1 = Permission(name='site-admin')
        p2 = Permission(name='site-auditor')
        u1 = UserRole(role='admin', desc='网站管理员')
        u2 = UserRole(role='auditor', desc='帖子审核员')
        for case in [p1, p2, u1, u2]:
            db.session.add(case)
        db.session.flush()
        db.session.add(RolePermission(role_id=u1.id, permission_id=p1.id))
        db.session.add(RolePermission(role_id=u2.id, permission_id=p2.id))
        db.session.commit()
    except Exception as e:
        click.echo('Error in initializing the database, please execute flask initdb to initialize the database before '
                   'performing this operation.')
