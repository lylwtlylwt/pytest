import os

#获取操作系统所有的环境变量
#print(os.environ)
#获取指定环境变量
#print(os.environ.get("APPDATA"))
#获取当前目录
#print(os.curdir)
#获取当前工作目录，即当前python脚本所在的目录
#print(os.getcwd())
#以列表的形式返回指定目录下的所有的文件
#print(os.listdir("../../../"))
#在当前目录下创建新目录
#os.mkdir("Lwttest")
#删除目录
#os.rmdir("F:\LWT\dev\pycharm_pro\pytest\lwttest")
#获取文件属性
#print(os.stat("F:\\LWT\\dev\\pycharm_pro\\pytest\\lwttest\\file.txt"))
#重命名
#os.rename("test1.txt","file.txt")
#删除普通文件
#os.remove("file.txt")
#运行shell(计算器)
#os.system("calc")
#查看当前的绝对路径
#print(os.path.abspath("."))
#拼接路径,参数2里没有要\
# p1 = r"F:\LWT\dev\pycharm_pro\pytest\lwttest"
# p2 = "test1.txt"
# print(os.path.join(p1,p2))
#拆分路径,拆最后的\后面的
# path2 = r"F:\LWT\dev\pycharm_pro\pytest\lwttest\test1.txt"
# print(os.path.split(path2))
#拆分扩展名
#print(os.path.splitext("test1.txt"))
#判断是否目录，true是目录，false不是目录
#print(os.path.isdir("test1"))
#判断文件是否存在,true存在，false不存在
#print(os.path.isfile(r"F:\LWT\dev\pycharm_pro\pytest\test.txt"))
#判断目录是否存在,true存在，false不存在
#print(os.path.isdir(r"F:\LWT\dev\pycharm_pro\pytest"))
#获取文件大小(单位:字节)
#print(os.path.getsize(r"F:\LWT\dev\pycharm_pro\pytest\test.txt"))
#获取文件的目录
#print(os.path.dirname(r"F:\LWT\dev\pycharm_pro\pytest\test.txt"))
#获取文件的名字
#print(os.path.basename(r"F:\LWT\dev\pycharm_pro\pytest\test.txt"))
