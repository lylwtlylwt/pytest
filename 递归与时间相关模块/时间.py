'''
常见的时间分为GMT、UTC、DST。
GMT，即格林尼治标准时间，也就是世界时。GMT的正午是指当太阳横穿格林尼治子午线（本初子午线）时的时间。但由于地球自转不均匀不规则，导致GMT不精确，现在已经不再作为世界标准时间使用。

UTC，即协调世界时。UTC是以原子时秒长为基础，在时刻上尽量接近于GMT的一种时间计量系统。为确保UTC与GMT相差不会超过0.9秒，在有需要的情况下会在UTC内加上正或负闰秒。UTC现在作为世界标准时间使用。

所以，UTC与GMT基本上等同，误差不超过0.9秒。
DST，即夏令时，是一种为节约能源而人为规定地方时间的制度。一般在天亮早的夏季人为将时间调快一小时，可以使人早起早睡，减少照明量，以充分利用光照资源，从而节约照明用电。各个采纳夏时制的国家具体规定不同。目前全世界有近110个国家每年要实行夏令时。


时间的表示形式：
1. 时间戳
    以整型或浮点型表示时间的一个以秒为单位的时间间隔的数值。这个时间间隔的基础值是从1970年1月1日零点开始算起。1就表示1970-01-01 00:00:01
    为什么要用1970年1月1日零点为基准呢？因为很多编程语言起源于UNIX系统，而UNIX系统认为1970年1月1日0点是时间纪元
2. 元组
    一种python的数据结构表示，这个元组有9个整型内容。
    year:   年
    month:  月
    day:    天
    hours:  小时
    minutes:分钟
    seconds:秒
    weekday:周
    Julian Day: 儒略日,是在儒略周期内以连续的日数计算时间的计时法，主要是天文学家在使用。
    flag(1、-1、0）:1表示夏令时，0表示标准时间，-1表示根据当前时间判断
3. 格式化字符串
      %a     本地(locale)简化星期名称
      %A     本地完整星期名称
      %b     本地简化月份名称
      %B     本地完整月份名称
      %c	 本地相应的日期和时间表示
      %d	 一个月中的第几天(01-31)
      %H     一天中的第几个小时(24小时制，00-23)
      %I     第几个小时(12小时制，01-12)
      %j     一年中的第几天(001-366)
      %m     月份(01-12)
      %M     分钟数(00-59)
      %p	 本地am或pm的相应符
      %S     秒(01-61)
      %U     一年中的星期数。(00-53星期天是一个星期的开始)，第一个星期天之前的所有天数都放在第0周
      %w     一个星期天中的第几天(0-6,0是星期天)
      %W     和%U基本相同，不同的是%W以星期一为一个星期的开始
      %x     本地相应日期
      %X     本地相应时间
      %y     去掉世纪的年份(00-99)
      %Y     完整的年份
      %Z     时区的名字(如果不存在为空字符)
      %%     ‘%’字符
'''
import time
import datetime
#返回当前时间的时间戳，浮点数形式，不需要参数
#print(time.time())
#将时间戳转换为UTC时间元组
#print(time.gmtime(time.time()))
#将时间戳转换为本地时间元组
#print(time.localtime(time.time()))
#将本地时间元组转换为时间戳
#print(time.mktime(time.localtime()))
#将时间元组转换为字符串
print(time.asctime(time.localtime()))
#将时间戳转换为字符串
print(time.ctime())
#将时间元组转换成给定格式的字符串，参数2为时间元组，如果没有参数2默认转换的是当前时间
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
#将时间字符串转换为时间元组
#print(time.strptime(time.strftime("%Y-%m-%d %H:%M:%S"),"%Y-%m-%d %H:%M:%S"))
#延迟一个时间，整型或者浮点型,单位是秒
#time.sleep()
#返回当前程序的CPU时间
#Unix形同始终返回全部的运行时间
#Windows从第二次开始，都是以第一个调用此函数的开始时间戳作为基数
# print(time.clock())
# sum = 0
# for i in range(100000000):
#     sum = sum+i
# print("执行用时:%d秒"%time.clock())
# d1 = datetime.datetime.strptime('2012-03-05 17:41:21', '%Y-%m-%d %H:%M:%S')
# d2 = datetime.datetime.strptime('2012-03-02 17:41:20', '%Y-%m-%d %H:%M:%S')
# delta = d1 - d2
# print(delta.seconds)

