with open('C:\\Users\\VIET\\Downloads\\Tp5\\phrases.txt','a')as fichier:
    res=input("est ce que tu veux ajouter des phrase au fichier phrases.txt ? O/N \n").lower()
    i=0
    if res=='o':
        nbr=int(input("Combien de phrases voulez-vous ajouter ?\nO"))
        for i in range(nbr):
            phrase=input(f"Entrez la phrase {i + 1} : ")
            fichier.write(phrase+"\n")
        print("les phrases ont été ajoutées avec succès.")
    else:
         print("aucune modification n'a été effectuée. Merci !")
