
print(int("1010",base =2))
#结果：10


#使用函数实现
def int2(str ,base = 2):
    return int(str,base)
print(int2("1011"))
#结果：11

import functools
#使用functools实现
int3 =functools.partial(int,base=2)
print(int3("1011"))