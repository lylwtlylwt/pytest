class Gun(object):
    def __init__(self,danjia):
        self.bulletbox = danjia

    def shoot(self):
        if self.bulletbox.bulletcount == 0:
            print("没有子弹了！")
        else:
            self.bulletbox.bulletcount -= 1
            print("子弹还有%d发！"%self.bulletbox.bulletcount)