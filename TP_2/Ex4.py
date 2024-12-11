class Personne:
    def __init__(self,nom,prenom,age):
        self.nom=nom
        self.prenom=prenom
        self.age=age
    def se_presenter(self):
        print(self.prenom," ",self.nom," agé(e) de ",self.age," ans.")
    
class Etudiant(Personne):
    def __init__(self,nom,prenom,age,matricule):
        super().__init__(nom,prenom,age)
        self.matricule=matricule
    def etudier(self):
        print(f"l'étudiant {self.prenom} {self.nom}, son matricule est {self.matricule}. il est en train d'étudier.")

personne = Personne("salma", "ramdi", 20)
personne.se_presenter()

etudiant = Etudiant("ilham", "bouaoud", 21, "D131261187")
etudiant.se_presenter()
etudiant.etudier()