def Fichier_Entier():
    while 1:
        try:
            file_name = input("Entrer le nom du fichier à lire : ")
            with open(file_name, 'r') as file:
                content = file.read()
            print("Contenu du fichier lu avec succès :")
            print(content)   
            break
        except FileNotFoundError:
            print(f"Erreur :le fichier {file_name} n'existe pas")
        except PermissionError:
            print(f"Erreur : Vous n'avez pas l'accee pour lire le fichier '{file_name}'.")
        except Exception as e:
            print(f"Erreur : {e}")
    
    while 1:
        try:
            user_input = input("Veuillez entrer un entier : ")
            nombre = int(user_input)
            print(f"Le nombre est : {nombre}")
            return
        except ValueError:
            print("Erreur : Entrer un nombre entier valide")
if __name__ == "__main__":
    Fichier_Entier()
