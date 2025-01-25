import os
ancien_nom = "C:\\Users\\VIET\\Downloads\\Tp5\\phrases.txt"
nouveau_nom = "C:\\Users\\VIET\\Downloads\\Tp5\\anciennes_phrases.txt"

try:
    os.rename(ancien_nom, nouveau_nom)
    print(f"Le fichier a été renommé")
except FileNotFoundError:
    print(f"Le fichier n'existe pas")
except IOError:
    print("Erreur lors du renommage du fichier")

try:
    os.remove(nouveau_nom)
    print(f"Le fichier a été supprimé")
except FileNotFoundError:
    print(f"Le fichier n'existe pas")
except IOError:
    print("Erreur lors de la suppression du fichier")
