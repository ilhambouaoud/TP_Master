from abc import ABC, abstractmethod

class Vehicule(ABC):
    @abstractmethod
    def deplacer(self):
        pass


class Voiture(Vehicule):
    def deplacer(self):
        return "La voiture roule sur la route..."


class Bicyclette(Vehicule):
    def deplacer(self):
        return "La bicyclette roule à l'aide de pédales..."


V = Voiture()
B = Bicyclette()

print(V.deplacer())   
print(B.deplacer()) 
