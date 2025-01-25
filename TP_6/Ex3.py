def read_file(filename):
    file = None 
    try:
        file = open(filename, 'r') 
        return file.read()          
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{filename}' n'existe pas !!!!")
    finally:
        if file: 
            file.close()
            print("Fichier fermé.")


filename = "exemple.txt"
contenu = read_file(filename)
if contenu:
    print("Contenu du fichier :", contenu)
