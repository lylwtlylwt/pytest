'''
如果不让内部的属性被外部直接访问，在属性前加两个下划线,在Python中如果在属性前加两个下划线，
那么这个属性就变成了私有属性
#不能直接访问per.__age是因为python解释器把__age变成了_Person__age
仍然可以用_Person__age去访问 ，但是强烈建议不要这么干，帅的人都不这么干
#在Python中 __XXX__被称为特殊变量，不是私有变量，只有变量名前加两个下划线的才是私有变量
#在Python中，_XXX变量(变量名前只有一个下划线)，在外部是可以被访问的。但是，按照约定的规则，
当我们看到这样的变量时，不要直接访问
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
print(per._Person__age)

