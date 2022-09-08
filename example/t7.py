
class A:

    def __init__(self):
        pass

    def __call__(self):
        print(1)


a = A()
print(2)
# 调用call的方法
a()
