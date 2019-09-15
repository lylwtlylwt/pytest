from father import Father
from mother import Mother
from child import Child

#child继承了两个父类：Father和Mother，两个父类都有Func方法，当子类调用func方法时，默认调用的是继承括号中的第一个父类
c = Child(1000,100)
print(c.faceValue,c.money)
c.eat()
c.play()
c.func()