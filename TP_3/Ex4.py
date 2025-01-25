class Produits:
    def __init__(self, nom, prix):
        self.__nom = nom
        self.set_prix(prix) 

    def get_nom(self):
        return self.__nom

    def get_prix(self):
        return self.__prix

    def set_nom(self, nom):
        self.__nom = nom

    def set_prix(self, prix):
        if prix >= 0:
            self.__prix = prix
        else:
            print("Erreur : Le prix ne peut pas être négatif.")
            self.__prix = 0  

    def calculerRemise(self, remise, seuil):
        if self.__prix > seuil:
            prix_remise = self.__prix * (1 - remise / 100)
            return prix_remise
        return self.__prix


if __name__ == "__main__":
    produit1 = Produits("Ordinateur", 60000)
    print(f"Prix avant remise : {produit1.get_prix()} DH")  
    prixRemise = produit1.calculerRemise(10, 1000)
    print(f"Prix après remise : {prixRemise} DH")
