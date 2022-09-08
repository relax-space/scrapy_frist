'''
验证 iter方法
'''

def a1():
    print(2)
    for i in [5,6,7]:
        yield i
    
def b1():
    a = iter(a1())
    print('1')
    b = next(a)
    print(b)

def b2():
    a = a1()
    print('1')
    b = next(a)
    print(b)
    
print('b1开始:')   
b1()
print('b2开始:')
b2()

