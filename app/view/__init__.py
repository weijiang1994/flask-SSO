"""
# coding:utf-8
@Time    : 2021/07/27
@Author  : jiangwei
@mail    : qq804022023@gmail.com
@File    : __init__.py.py
@Desc    : __init__.py
@Software: PyCharm
"""
from flask import Blueprint, render_template


sso = Blueprint('sso', __name__, url_prefix='/oauth')


@sso.route('/login/')
def oauth():
    return render_template('base.html')
