from person import Person
from gun import Gun
from bulletbox import Bulletbox

class Hunter(Person):
    def __init__(self,gun,guname):
        super(Hunter, self).__init__(gun)
        self.guname = guname


bul = Bulletbox(5)
gun = Gun(bul)
per = Hunter(gun,'R')

per.fire()
per.fire()
per.fire()
per.fire()
per.fire()
per.fire()

