import os
from datetime import datetime
import math

print("Current file : ",os.getcwd())# Afficher le répertoire actuel du fichier Python

now = datetime.now()#obtenir la date et l'heure actuelles
print("date time : ",now)

a=int(input("Donner un nombre : "))
sqrt= math.sqrt(a) #calculer la racine carrée de a
print("la racine carré de ",a," est : ",sqrt )
