'''
datetime比time高级不少，可以理解为datatime基于time进行了封装，
提供了更为实用的函数，datetime模块的接口更为直观，更容易调用

模块中的类：
datetime      同时有时间和日期
timedelta     主要用于计算时间的跨度
tzinfo        时区相关
time          只关注时间
date          只关注日期
'''
import datetime

#获取当前时间
#d1 = datetime.datetime.now()
#获取指定时间 年,月,日,时,分,秒,毫秒
#d1 = datetime.datetime(1999,10,1,10,28,25,123456)
#将时间转为字符串
#d1 = datetime.datetime.now().strftime("%Y-%m-%d %X")

#将格式化字符串转为datetime对象
#注意：
#d1 = datetime.datetime.strptime(datetime.datetime.now().strftime("%Y-%m-%d %X"),"%Y-%m-%d %X")

#时间加减
# d1 = datetime.datetime(1999,10,1,10,28,25,123456)
# d2 = datetime.datetime.now()
# d3 = d2 - d1
# print("d2和d1间隔--总时长：",d3)
# print("d2和d1间隔--总时长取天数：",d3.days)
# print("d2和d1间隔--总时间长取秒数(不是总共间隔多少秒)：",d3.seconds)
# print("d2和d1间隔--总时长(单位秒)：",d3.total_seconds())


