#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2025/11/9 17:32
@Author  : 510195171@qq.com
@File    : __init__.py.py
"""
#  . 代表从当前文件夹下找
from .app_handler import AppHandler

# __all__ 导出传递的所有包
# 导出 AppHandler
__all__ = ["AppHandler"]
