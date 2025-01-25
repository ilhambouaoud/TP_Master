import math

class Forme:
    def calculer_surface(self):
        raise NotImplementedError("!!!")

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

class Triangle(Forme):
    def __init__(self, base, hauteur):
        self.base = base
        self.hauteur = hauteur

    def calculer_surface(self):
        return (self.base * self.hauteur) / 2

def afficher_surface(formes):
    for forme in formes:
        try:
            surface = forme.calculer_surface()
            print(f"Surface de la forme : {surface:.2f}")
        except NotImplementedError as e:
            print(f"Erreur : {e}")
        except AttributeError:
            print("L'objet doit être une forme valide!")

formes = [
    Cercle(5),
    Rectangle(4, 6),
    Triangle(3, 7)
]

afficher_surface(formes)
