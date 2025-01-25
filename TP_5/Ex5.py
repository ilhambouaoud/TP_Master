import json 
donnees={
    "etudiants": [
        {"nom": "ilham","age": 21,"note": 19.5},
        {"nom": "naima","age": 23,"note": 17.0},
        {"nom": "mohammed","age": 20,"note": 14.0}
    ]
}
with open('C:\\Users\\VIET\\Downloads\\Tp5\\etudiants.json','w')as fichier:
    donnees=json.dump(donnees,fichier,indent=2)
with open('C:\\Users\\VIET\\Downloads\\Tp5\\etudiants.json','r')as fichier:
    donnees=json.load(fichier)
    print(donnees)
    