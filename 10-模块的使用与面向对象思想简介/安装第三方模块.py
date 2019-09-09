'''
Mac:无需安装
Linux:无需安装
Windows:勾选了pip和Add python.exe to Path
 '''
#要安装三方模块，需要知道模块的名字
#Pillow 非常强大的处理图像的工具库

from PIL import Image

#打开图片
im = Image.open("img1.jpg")
#查看图片的信息
print(im.format, im.size, im.mode)
#设置图片的大小
im.thumbnail(150,100)
im.save("temp.jpg", "JPEG")