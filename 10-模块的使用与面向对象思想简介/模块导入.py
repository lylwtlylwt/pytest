#import 模块名
#导入模块的所有对象，对象引用时前面需要加上模块名

#from... import *语句
#把一个模块中所有的内容全部导入当前命名空间，不推荐这种写法(以*导入)

#from... import 对象
#把一个模块中指定的对象导入到当前命名空间


import moudles

def hello():
    print("Hello Lwt")

moudles.hello()