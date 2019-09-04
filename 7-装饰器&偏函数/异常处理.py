try:
    print(3/1)
except  ZeroDivisionError as e:
    print("除数为0")
else:
    print("没有错误")
finally:
    print("最后打印")