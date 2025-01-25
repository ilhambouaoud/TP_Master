import csv
contacts = [
    ["Nom","Age","Ville"],
    ["Ilham", 21, "Agadir"],
    ["Naima", 50, "Taghazout"]
]
with open("C:\\Users\\VIET\\Downloads\\Tp5\\contact.csv",mode='w',newline="")as fichier:
    ajoute=csv.writer(fichier)
    ajoute.writerows(contacts)
    
with open("C:\\Users\\VIET\\Downloads\\Tp5\\contact.csv",mode='r',newline="")as fichier:
    ligne=csv.reader(fichier)
    for i in ligne:
        print(i)