'''
self代表类的实例，而非类
哪个对象调用方法，那么该方法中的self就代表那个对象
#Self不是关键字，换成其他的标识符也是可以的，但帅的人一般都用self
self.__class__ 代表类名

'''

class Person(object):

    def __init__(self):
     self.age = 18
     self.name = ""

p1 = Person()
print(p1.age)
p1.age = 10
print(p1.age)
print(p1.__class__)