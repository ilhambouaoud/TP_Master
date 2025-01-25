def get_positive_integer():
    while 1:
        try:
            user_input = input("Entrer un entier positif : ")
            number = int(user_input)
            if number > 0:
                return number
            else:
                print("Le nombre doit être positif!!!!")
        except ValueError:
            print("Erreur : la valeur doit etre un nombre entier valide")

if __name__ == "__main__":
    res = get_positive_integer()
    print(f"Nombre entier est : {res}")
