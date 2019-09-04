'''
path =r"F:\LWT\dev\pycharm_pro\pytest\7-装饰器&偏函数\file1.txt"

with open(path,"wb") as f1:
    str ="今天08-15天气很晴朗11！"
    f1.write(str.encode("utf-8"))
'''
import pickle

path =r"F:\LWT\dev\pycharm_pro\pytest\7-装饰器&偏函数\file1.txt"
mylist = [1,2,3,4,5,"今年是2019年！ "]
f = open(path,"wb")
pickle.dump(mylist,f)
f.close()

f0 = open(path,"rb")
templist = pickle.load(f0)
print(templist)
f0.close()

with open(path,"rb") as f1:
    data = f1.read()
    print("f1:",data)