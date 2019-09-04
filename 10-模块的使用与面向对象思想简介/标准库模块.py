import sys


list = sys.argv
num = len(list)
for r in range(0,num):
    print("第%d个参数:"%r,list[r])