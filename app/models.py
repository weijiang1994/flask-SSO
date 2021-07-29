"""
# coding:utf-8
@Time    : 2021/07/27
@Author  : jiangwei
@mail    : qq804022023@gmail.com
@File    : models.py
@Desc    : models
@Software: PyCharm
"""
from app.extensions import db
from flask_login import UserMixin
import datetime


class User(db.Model, UserMixin):
    __tablename__ = 't_user'

    id = db.Column(db.INTEGER, primary_key=True, index=True, autoincrement=True)
    username = db.Column(db.String(50), default='', nullable=False, unique=True)
    nickname = db.Column(db.String(50), default='')
    email = db.Column(db.String(128), default='', nullable=False, unique=True)
    password = db.Column(db.String(512), default='', nullable=False)
    gender = db.Column(db.INTEGER, default=1, comment='1: male 0:female')
    c_time = db.Column(db.DateTime, default=datetime.datetime.now)
    active = db.Column(db.INTEGER, default=1, comment='1: activate 0: dismiss')

    member_ship = db.relationship('MemberShip', back_populates='user')


class MemberShip(db.Model):
    __tablename__ = 't_member_ship'
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    user_id = db.Column(db.INTEGER, db.ForeignKey('t_user.id'))
    group_id = db.Column(db.INTEGER, db.ForeignKey('t_user_role.id'))

    user = db.relationship('User', back_populates='member_ship')
    role = db.relationship('UserRole', back_populates='member_ship')


class Permission(db.Model):
    __tablename__ = 't_permission'

    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False, default='', unique=True)
    c_time = db.Column(db.DateTime, default=datetime.datetime.now)

    role_permission = db.relationship('RolePermission', back_populates='permission')

    def __init__(self, name, c_time=datetime.datetime.now()):
        self.name = name
        self.c_time = c_time


class UserRole(db.Model):
    __tablename__ = 't_user_role'

    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True, nullable=False)
    role = db.Column(db.String(128), nullable=False, default='', unique=True)
    desc = db.Column(db.Text, nullable=True, default='')
    c_time = db.Column(db.DateTime, default=datetime.datetime.now)

    member_ship = db.relationship('MemberShip', back_populates='role')
    role_permission = db.relationship('RolePermission', back_populates='role')


class RolePermission(db.Model):
    __tablename__ = 't_role_permission'

    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True, nullable=False)
    role_id = db.Column(db.INTEGER, db.ForeignKey('t_user_role.id'))
    permission_id = db.Column(db.INTEGER, db.ForeignKey('t_permission.id'))

    role = db.relationship('UserRole', back_populates='role_permission')
    permission = db.relationship('Permission', back_populates='role_permission')


class Client(db.Model):
    __tablename__ = 't_client'

    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    name = db.Column(db.String(512), default='', nullable=False)
    client_id = db.Column(db.INTEGER, nullable=False)
    client_secret = db.Column(db.String(512), nullable=False)
    callback = db.Column(db.String(512), default='')
