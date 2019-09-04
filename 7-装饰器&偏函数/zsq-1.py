'''
装饰器： 是一个闭包，把一个函数当做参数返回一个替代版的函数，
本质上就是一个返回函数的函数
'''



def outer(func):
    print("outer开始")
    def inner(*name,**age):
        print("age被改变")
        func(*name,**age)
        print("inner.func被执行")
    return inner
    print("outer结束")

@outer
def say(name,age,cla):
    print("%s is %d years old,in class %s"%(name,age,cla))

# s = outer(say)
# s(-11)
say('sunc',19,'computer')
