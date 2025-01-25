try:
    with open("inexistant.txt", "r") as fichier:
        contenu = fichier.read()
        print(contenu)
except FileNotFoundError:
    print("Erreur : Le fichier 'inexistant.txt' n'existe pas.")
except IOError:
    print("Erreur lors de l'ouverture du fichier.")
