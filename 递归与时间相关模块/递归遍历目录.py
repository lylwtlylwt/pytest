import os

def getAllDir(path,sp = ""):
    #得到当前目录下所有的文件
    fileList = os.listdir(path)
    #处理每一个文件
    sp = sp + " "
    for fileName in fileList:
        #判断是否是路径(用绝对路径)
        fileAbsPath = os.path.join(path,fileName)
        if os.path.isdir(fileAbsPath):
            print(sp + "目录：",fileName)
            #递归调用
            getAllDir(fileAbsPath, sp)
        else:
            print("普通文件:",fileName)


getAllDir(r"F:\LWT\books\Kindle")
