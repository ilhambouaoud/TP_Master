class Chien:
    def __init__(self,nom, race,age):
        self.nom=nom
        self.race=race
        self.age=age
    def aboyer(self):
        print("Woof!")

c1=Chien("rokey","champolice",2)
c1.aboyer()