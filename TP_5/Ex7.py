import shutil
import os

journal_path = r"C:\Users\VIET\Downloads\Tp5\journal.txt"
copie_path = r"C:\Users\VIET\Downloads\Tp5\journal_copie.txt"
destination = r"C:\Users\VIET\Desktop\fichier_deplace"

try:
    if os.path.exists(journal_path):
        shutil.copy(journal_path, copie_path)
        print("Le fichier a été copié.")
    else:
        print(f"Le fichier source n'existe pas.")
except IOError:
    print("Erreur lors de la copie du fichier.")

try:
    if not os.path.exists(destination):
        os.makedirs(destination)
    
    shutil.move(copie_path, destination)
    print("Le fichier a été déplacé.")
except FileNotFoundError:
    print(f"Le fichier à déplacer n'existe pas.")
except IOError:
    print("Erreur lors du déplacement du fichier.")
