
class Produit:
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix

    def __str__(self):
        return f"{self.nom} - {self.prix}€"

class Commande:
    def __init__(self, produit, quantite):
        self.produit = produit
        self.quantite = quantite

    def total(self):
        return self.produit.prix * self.quantite

    def __str__(self):
        return f"{self.quantite} x {self.produit.nom} = {self.total()}€"


class Panier:
    def __init__(self):
        self.commandes = []

    def ajouter_commande(self, commande):
        self.commandes.append(commande)

    def total_panier(self):
        return sum(commande.total() for commande in self.commandes)

    def afficher_panier(self):
        for commande in self.commandes:
            print(commande)
        print(f"Total du panier: {self.total_panier()}€")


produit1 = Produit("Chemise", 20)
produit2 = Produit("Jeans", 50)

commande1 = Commande(produit1, 2)
commande2 = Commande(produit2, 1)

panier = Panier()
panier.ajouter_commande(commande1)
panier.ajouter_commande(commande2)

panier.afficher_panier()
