class CompteBancaire:
    def __init__(self,titulaire,solde):
        self.titulaire=titulaire
        self.solde=solde

    def deposer(self,montant):
        self.solde+=montant
    def retirer(self,montant):
        if self.solde>=montant:
            self.solde-=montant
        else :
            print("solde insuffisant")
    def afficher_solde(self):
        print("votre solde est : ", self.solde);

Compte=CompteBancaire("ilham bouaoud",500000)
Compte.deposer(200)
Compte.retirer(300)
Compte.afficher_solde()
Compte.retirer(600000)
