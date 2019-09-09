'''
实例化对象
格式： 对象名 = 类名(参数列表)
注意：没有参数，小括号也不能省略
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


per1 = Person()
print(per1)
print(type(per1))
print(id(per1))

per2 = Person()
print(per2)
print(type(per2))
print(id(per2))

