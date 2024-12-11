class Personne:
    def __init__(self, nom):
        self.nom = nom
        self.amis = []

    def ajouter_ami(self, ami):
        if ami not in self.amis:
            self.amis.append(ami)
            print(f"{ami} a été ajouté à la liste des amis de {self.nom}.")
        else:
            print(f"{ami} est déjà un ami.")

    def afficher_amis(self):
        if not self.amis:
            print(f"{self.nom} n'a pas d'amis.")
        else:
            print(f"Les amis de {self.nom} :")
            for ami in self.amis:
                print(f"- {ami}")

personne = Personne("ilham")
personne.ajouter_ami("salma")
personne.ajouter_ami("fatima zahrae")
personne.afficher_amis()
