'''
dir 用法
'''

from asset import b1

for k in dir(b1):
    v = getattr(b1, k)
    print(k, type(v), v)
