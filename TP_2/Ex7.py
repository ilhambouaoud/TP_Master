class Livre:
    def __init__(self, titre, auteur, annee_publication):
        self.titre = titre
        self.auteur = auteur
        self.annee_publication = annee_publication


class Bibliotheque:
    def __init__(self):
        self.livres = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)
        print(f"Le livre '{livre.titre}' de {livre.auteur} ({livre.annee_publication}) a été ajouté à la bibliothèque.")

    def afficher_livres(self):
        if not self.livres:
            print("La bibliothèque est vide.")
        else:
            print("Livres dans la bibliothèque :")
            for livre in self.livres:
                print(f"- {livre.titre} de {livre.auteur} ({livre.annee_publication})")


livre1 = Livre("la boite a merveille", "Mohammed Sefriuoi", 1954)
livre2 = Livre("Antigon", "Jean", 1924)

biblio = Bibliotheque()
biblio.ajouter_livre(livre1)
biblio.ajouter_livre(livre2)
biblio.afficher_livres()