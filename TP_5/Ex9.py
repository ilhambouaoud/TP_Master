fichier_path = "C:\\Users\\VIET\\Downloads\\Tp5\\fichier1.txt"

nombre_lignes = 0
nombre_mots = 0
nombre_caracteres = 0

try:
    with open(fichier_path, 'r') as fichier:
        for ligne in fichier:
            nombre_lignes += 1
            nombre_caracteres += len(ligne)
            nombre_mots += len(ligne.split())

    print(f"Nombre total de lignes : {nombre_lignes}")
    print(f"Nombre total de mots : {nombre_mots}")
    print(f"Nombre total de caractères : {nombre_caracteres}")

except FileNotFoundError:
    print("Erreur : Le fichier spécifié n'existe pas.")
except IOError:
    print("Erreur lors de la lecture du fichier.")
