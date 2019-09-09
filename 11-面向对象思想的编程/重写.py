'''
重写：将函数重新定义写一遍
__str__():在调用print打印对象时自动调用，是给用户用的，是一个描述对象的方法
__repr__():是给机器用的，在Python解释器里面直接敲对象名在回车后调用的方法
注意：在没用str时，且有repr, repr=str
优点：当一个对象的属性值很多，并且都南非要打印，重写了__str__方法后，简化了代码
'''

class Person(object):
    def __init__(self,name,age,height,weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def __repr__(self):
        return "姓名：%s \n年龄：%d\n身高：%d\n体重：%d"%(self.name, self.age, self.height, self.weight)

    def __str__(self):
        return "str"
per = Person("Lee", 20, 170, 60)
#实际调用的是per.__str__()
print(per)