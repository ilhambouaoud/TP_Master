class Personne:
    def __init__(self, nom, prenom, age):
        self.__nom = nom
        self.__prenom = prenom
        self.__age = age
    def get_nom(self):
        return self.__nom
    def set_nom(self,nom):
        self.__nom=nom 

    def get_prenom(self):
        return self.__prenom
    def set_prenom(self,prenom):
        self.__prenom=prenom 

    def get_age(self):  
        return self.__age

    def set_age(self, age):
        self.__age = age


p= Personne("ilham", "bou", 25)

print("Nom :", p.get_nom())#p.nom si les attributs pubic 
print("Prénom :", p.get_prenom())
print("Âge :", p.get_age())


p.set_nom("aaaaa")
p.set_prenom("bbb")
p.set_age(30)
#personne.age=33 pour les attribut public

print("\nNom modifié :", p.get_nom())
print("Prénom modifié :", p.get_prenom())
print("Âge modifié :", p.get_age())


