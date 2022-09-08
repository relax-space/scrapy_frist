'''
对象的hash值: 如果对象不重写__hash__方法, 同一个对象的哈希值是一样的
'''


class A1:
    a = 1
    pass

    # def __hash__(self) -> int:
    #     return hash(self.a)


a1 = A1()
print(hash(a1))

a1.a = 5
print(hash(a1))

b1 = A1()

print(hash(b1))
