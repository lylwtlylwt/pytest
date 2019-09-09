'''
访问属性：
    格式：对象名.属性名
    赋值：对象名.属性名 = 新值
访问方法：
    格式：对象名.方法
'''
'''
构造函数： __init__() 在使用类创建对象的时候自动调用
注意：如果不显示的写出构造函数，默认会自动添加一个空的构造函数

析构函数:__del__() 释放对象时自动调用
'''
class Person(object):
    #定义属性
    name =""
    age = 0
    height = 0
    weight =0
    #定义方法
    def run(self):
        print("run")

    def eat(self, food):
        print("eat " + food)

    def __init__(self,name,age):
        self.name=name
        self.age=age
        pass
    def __del__(self):
        print("调用析构函数，资源释放")



per = Person('Hi',18)
print(per.name,per.age)
del per
#print(per.age)

#在函数里定义的对象，会在函数结束时自动释放，这样可以用来减少内存空间的浪费
def func():
    per2 =Person("Hi1",12)
func()
