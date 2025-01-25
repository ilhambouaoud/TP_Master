with open("C:\\Users\\VIET\\Downloads\\Tp5\\phrases.txt","w")as fichier:
    phrase1=input("Entrer première phrase...\n")
    phrase2=input("Entrer première phrase...\n")
    phrase3=input("Entrer première phrase...\n")
    fichier.write(phrase1+"\n")
    fichier.write(phrase2+"\n")
    fichier.write(phrase3+"\n")
    #fichier.writelines([phrase1 + "\n", phrase2 + "\n", phrase3 + "\n"])
