#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2025/11/9 17:54
@Author  : 510195171@qq.com
@File    : router.py
"""
from dataclasses import dataclass

from flask import Flask, Blueprint
from injector import inject

from internal.handler import AppHandler


@inject
@dataclass
class Router:
    """路由"""
    # 使用 @inject + @dataclass 依赖注入控制器
    app_handler: AppHandler

    def register_router(self, app=Flask):
        """注册路由"""
        # 1. 注册一个蓝图
        bp = Blueprint("llmops", __name__, url_prefix="")

        # 2. 将url 与对应的控制器方法绑定
        bp.add_url_rule("/ping", view_func=self.app_handler.ping)

        # 3. 在应用上注册蓝图
        app.register_blueprint(bp)
