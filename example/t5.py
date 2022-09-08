'''
测试1: import_module
测试2: cast
'''

from importlib import import_module
from typing import cast

from asset.b3 import A1, B1

b3= import_module('asset.b3')
a1_cls = getattr(b3,'A1')
print(a1_cls().a())

# 测试cast, 下面代码把A1改成B1,仍然执行正确结果
a2_cls = cast(A1,a1_cls)
print(a2_cls().a())
