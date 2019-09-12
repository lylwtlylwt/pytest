from police import Police
class Policeman(Police):
    def __init__(self, name ,age):
        super(Policeman, self).__init__(name,age)

p1 = Policeman("Lee", 10)

p1.eat("APPLE")