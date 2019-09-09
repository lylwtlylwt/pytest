'''
如果不让内部的属性被外部直接访问，在属性前加两个下划线,在Python中如果在属性前加两个下划线，
那么这个属性就变成了私有属性
'''

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.__age = age
#通过内部的方法，去修改私有属性
#通过自定义的方法实现对私有属性的赋值与取值
    def setAge(self,age):
        if age <18:
            self.age = 18

    def eat(self, food):
        print("eat "+food)



per = Person("Lee",100)


