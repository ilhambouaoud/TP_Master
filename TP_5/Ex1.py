with open("C:\\Users\\VIET\\Downloads\\Tp5\\fichier1.txt","r") as fichier:
    ligne=fichier.readline()
    i=1;
    while ligne:
        print(i," ",ligne.strip())
        i+=1;
        ligne=fichier.readline()