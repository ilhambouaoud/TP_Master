import csv

fichier_contacts = "contacts.csv"

def ajouter_contact():
    nom=input("Entrer nom de contact : ")
    age=input("Entrer l'age de contact : ")
    ville=input("Entrer ville de contact : ")
    with open("contacts.csv",mode="a",newline="")as fichier:
        contact=csv.writer(fichier)
        contact.writerow([nom,age,ville])
    print("Le contact a été ajouté avec succès.")


def afficher_contacts():
    try:
        with open(fichier_contacts, mode='r', newline='') as fichier:
            reader = csv.reader(fichier)
            for row in reader:
                print(f"Nom : {row[0]}, Âge : {row[1]}, Ville : {row[2]}")
    except FileNotFoundError:
        print("Le fichier n'existe pas!!!")

def rechercher_contact():
    recherche = input("Entrez le nom du contact à rechercher : ")
    try:
        with open(fichier_contacts, mode='r', newline='') as fichier:
            reader = csv.reader(fichier)
            found = False
            for row in reader:
                if row[0].lower() == recherche.lower():
                    print(f"Nom : {row[0]}, Âge : {row[1]}, Ville : {row[2]}")
                    found = True
            if not found:
                print("le nom de ce contact n'existe pas")
    except FileNotFoundError:
        print("Le fichier n'existe pas.")

def supprimer_contact():
    recherche = input("Entrez le nom du contact à supprimer : ")
    try:
        with open(fichier_contacts, mode='r', newline='') as fichier:
            rows = list(csv.reader(fichier))
        with open(fichier_contacts, mode='w', newline='') as fichier:
            writer = csv.writer(fichier)
            found = False
            for row in rows:
                if row[0].lower() == recherche.lower():
                    found = True
                    continue
                writer.writerow(row)
            if found:
                print("Contact supprimé avec succès")
            else:
                print("le nom de ce contact n'existe pas dans la liste des contactes")
    except FileNotFoundError:
        print("Le fichier n'existe pas")

def menu():
    while True:
        print("---------Menu------------")
        print("1 ---Ajouter un contact")
        print("2 ---Afficher tous les contacts")
        print("3 ---Rechercher un contact")
        print("4 ---Supprimer un contact")
        print("5 ---Quitter")
        
        choix = input("Choisissez une option (1-5) : ")
        
        if choix == '1':
            ajouter_contact()
        elif choix == '2':
            afficher_contacts()
        elif choix == '3':
            rechercher_contact()
        elif choix == '4':
            supprimer_contact()
        elif choix == '5':
            print("Vous aver quitter!!!")
            break
        else:
            print("Option invalide")

menu()
