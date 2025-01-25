from abc import ABC, abstractmethod
import math

class Forme(ABC):
    @abstractmethod
    def calculer_surface(self):
        pass

class Cercle(Forme):
    def __init__(self, rayon):
        self.rayon = rayon

    def calculer_surface(self):
        return math.pi * (self.rayon ** 2)

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def calculer_surface(self):
        return self.largeur * self.hauteur

cercle = Cercle(5)
print("Surface du cercle :", cercle.calculer_surface())

rectangle = Rectangle(4, 7)
print("Surface du rectangle :", rectangle.calculer_surface())
