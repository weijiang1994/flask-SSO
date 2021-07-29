"""
# coding:utf-8
@Time    : 2021/07/27
@Author  : jiangwei
@mail    : qq804022023@gmail.com
@File    : extensions.py
@Desc    : extensions
@Software: PyCharm
"""
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
db = SQLAlchemy()
mg = Migrate()
