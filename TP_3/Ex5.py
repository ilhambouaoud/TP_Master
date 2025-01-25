class Employe:
    def __init__(self, nom, prenom, salaire):
        self.nom = nom
        self.prenom = prenom
        self.salaire = salaire

    def afficher_details(self):
        print(f"Nom : {self.nom}, Prénom : {self.prenom}, Salaire : {self.salaire:.2f} DH")


class Manager(Employe):
    def __init__(self, nom, prenom, salaire):
        super().__init__(nom, prenom, salaire)
        self.E_supervises = []  

    def ajouter_employe(self, employe):
        if isinstance(employe, Employe):
            self.E_supervises.append(employe)
            print(f"Employé {employe.prenom} {employe.nom} ajouté sous la supervision de {self.prenom} {self.nom}.")
        else:
            print("Erreur : il doit être une instance de la classe Employe!!!!")

    def afficher_employes_supervises(self):
        if self.E_supervises:
            print(f"Manager {self.prenom} {self.nom} supervise les employés suivants :")
            for employe in self.E_supervises:
                employe.afficher_details()
        else:
            print(f"Manager {self.prenom} {self.nom} ne supervise aucun employé.")

if __name__ == "__main__":
    employe1 = Employe("mohammed", "mohammed", 35000)
    employe2 = Employe("naima", "naila", 42000)
    employe3 = Employe("abdo", "abdo", 38000)

    
    manager1 = Manager("ilham", "bouaoud", 60000)

    manager1.ajouter_employe(employe1)
    manager1.ajouter_employe(employe2)

    manager1.afficher_employes_supervises()


