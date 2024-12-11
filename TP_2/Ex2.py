class Voiture:
    def __init__(self,marque,modèle,année):
        self.marque=marque
        self.modèle=modèle
        self.année=année

    def afficher_info(self):
        print("la marque de voiture est : ",self.marque," le modèle est : ",self.modèle," de ",self.année)

v1= Voiture("Toyota","Toyota Corolla",2023)
v2=Voiture("Volkswagen","Volkswagen golf",2023)
v3=Voiture("BMW","BMW x5",2022)

v1.afficher_info()
v2.afficher_info()
v3.afficher_info()