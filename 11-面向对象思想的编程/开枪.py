from person import Person
from gun import Gun
from bulletbox import Bulletbox

bul = Bulletbox(5)
gun = Gun(bul)
per = Person(gun)

per.fire()
per.fire()
per.fire()
per.fire()
per.fire()
per.fire()
per.fire()