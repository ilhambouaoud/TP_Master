import pandas as pd #pip install pandas (il faut install biblio)

fichier = pd.read_csv("employes.csv")

print("Les cinq premières lignes du fichier CSV :")
print(fichier.head())#head : pour afficher les premières lignes par defaut (5)

moyenne_age = fichier["age"].mean() # calcule la moyenne de la colonne age.
print(f"\nLa moyenne d'âge des employés est de {moyenne_age:.2f} ans")
