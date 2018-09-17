#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Blueprint
from flask import render_template
from flask import request

account = Blueprint('account', __name__)

# 蓝图里面可以个性化定制，和外部的init设置成不一样的
# account = Blueprint('account', __name__, url_prefix='/acc', template_folder='tpls')

@account.route('/login.html', methods=['GET', "POST"])
def login():
    return render_template('login.html')
