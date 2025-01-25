class Vehicule:
    def __init__(self,marque,modele,annee):
        self.marque=marque
        self.modele=modele
        self.annee=annee
    def afficher_info(self):
        print(f"Marque => {self.marque}, Modèle => {self.modele}, Année => {self.annee}")

class Moteur:
    def __init__(self,puissance,type_moteur):
        self.puissance=puissance
        self.type_moteur=type_moteur
    def afficher_info(self):
        print(f"Puissance => {self.puissance} chevaux, Type de moteur => {self.type_moteur}")

class Voiture:
    def __init__(self,marque,modele,annee,puissance,type_moteur,nombre_de_places):
        Vehicule.__init__(self,marque,modele,annee)
        Moteur.__init__(self,puissance,type_moteur)
        self.nombre_de_places=nombre_de_places
    def afficher_info(self):
        print("--Les informations de voiture : ")
        Vehicule.afficher_info(self)#super().afficher_info() 
        Moteur.afficher_info(self)
        print(f"Nombre de places => {self.nombre_de_places}")

class Moto:
    def __init__(self,marque,modele,annee,puissance,type_moteur,type_moto):
        Vehicule.__init__(self,marque,modele,annee)
        Moteur.__init__(self,puissance,type_moteur)
        self.type_moto=type_moto
    def afficher_info(self):
        print("\n--Les informations de moto : ")
        Vehicule.afficher_info(self)
        Moteur.afficher_info(self)
        print(f"Type de moto => {self.type_moto}")

    
voiture = Voiture("BMW", "X5", 2022, 300, "Essence", 5)
voiture.afficher_info()

moto = Moto("Yamaha", "R1", 2021, 200, "Essence", "Sport")
moto.afficher_info()

print(Voiture.mro())