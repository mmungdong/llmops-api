#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2025/11/9 18:12
@Author  : 510195171@qq.com
@File    : http.py
"""
from flask import Flask

from internal.router import Router


class Http(Flask):
    """Http 服务器"""

    def __init__(self, import_name: str, *args, router: Router, **kwargs):
        super().__init__(import_name)
        router.register_router(self)
