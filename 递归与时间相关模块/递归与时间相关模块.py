

'''
写递归函数的方式：
1. 写出临界条件
2.找这一次和上一次的关系
3.假设当前已经能用，调用自身计算上一次的结果，再求出本次的结果
'''
#输入一个数(大于等于1)，求1+2+3+....+n的和
##普通写法
def sum(n):
    sum = 0
    for x in range(1,n+1):
        sum += x
    return sum

#递归的写法
def sum2(n):
    if n == 1:
        return  1
    else:
        return n+sum2(n-1)

