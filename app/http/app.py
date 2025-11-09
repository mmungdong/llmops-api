#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2025/11/9 18:15
@Author  : 510195171@qq.com
@File    : app.py
"""

from injector import Injector

from internal.router import Router
from internal.server import Http

injector = Injector()

app = Http(__name__, router=injector.get(Router))

# 这个判断当作为main方法时才会运行，如果被引用，则这段代码不会执行
if __name__ == "__main__":
    app.run(debug=True)
